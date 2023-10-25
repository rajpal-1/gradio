import time

import gradio_client as grc
from fastapi.testclient import TestClient

import gradio as gr


class TestQueueing:
    def test_single_request(self):
        with gr.Blocks() as demo:
            name = gr.Textbox()
            output = gr.Textbox()

            def greet(x):
                return f"Hello, {x}!"

            name.submit(greet, name, output)

        demo.launch(prevent_thread_lock=True)

        client = grc.Client(f"http://localhost:{demo.server_port}")
        job = client.submit("x", fn_index=0)

        assert job.result() == "Hello, x!"

    def test_multiple_requests(self):
        with gr.Blocks() as demo:
            name = gr.Textbox()
            output = gr.Textbox()

            def greet(x):
                time.sleep(2)
                return f"Hello, {x}!"

            name.submit(greet, name, output)

        app, _, _ = demo.queue(concurrency_count=2).launch(prevent_thread_lock=True)
        test_client = TestClient(app)

        client = grc.Client(f"http://localhost:{demo.server_port}")
        client.submit("a", fn_index=0)
        job2 = client.submit("b", fn_index=0)
        client.submit("c", fn_index=0)
        job4 = client.submit("d", fn_index=0)

        sizes = []
        while job4.status().code.value != "FINISHED":
            queue_status = test_client.get("/queue/status").json()
            sizes.append(queue_status["queue_size"])
            time.sleep(0.05)

        assert max(sizes) in [
            2,
            3,
            4,
        ]  # Can be 2 - 4, depending on if the workers have picked up jobs before the queue status is checked
        assert min(sizes) == 0
        assert sizes[-1] == 0

        assert job2.result() == "Hello, b!"
        assert job4.result() == "Hello, d!"

    def test_all_status_messages(self):
        with gr.Blocks() as demo:
            name = gr.Textbox()
            output = gr.Textbox()

            def greet(x):
                time.sleep(2)
                return f"Hello, {x}!"

            name.submit(greet, name, output)

        app, _, _ = demo.queue(concurrency_count=2).launch(prevent_thread_lock=True)
        test_client = TestClient(app)

        client = grc.Client(f"http://localhost:{demo.server_port}")
        client.submit("a", fn_index=0)
        job2 = client.submit("b", fn_index=0)
        client.submit("c", fn_index=0)
        job4 = client.submit("d", fn_index=0)

        sizes = []
        while job4.status().code.value != "FINISHED":
            queue_status = test_client.get("/queue/status").json()
            sizes.append(queue_status["queue_size"])
            time.sleep(0.05)

        assert max(sizes) in [
            2,
            3,
            4,
        ]  # Can be 2 - 4, depending on if the workers have picked up jobs before the queue status is checked
        assert min(sizes) == 0
        assert sizes[-1] == 0

        assert job2.result() == "Hello, b!"
        assert job4.result() == "Hello, d!"

    def test_every_does_not_block_queue(self):
        with gr.Blocks() as demo:
            num = gr.Number(value=0)
            num2 = gr.Number(value=0)
            num.submit(lambda n: 2 * n, num, num, every=0.5)
            num2.submit(lambda n: 3 * n, num, num)

        app, _, _ = demo.queue(max_size=1).launch(prevent_thread_lock=True)
        test_client = TestClient(app)

        client = grc.Client(f"http://localhost:{demo.server_port}")
        job = client.submit(1, fn_index=1)

        for _ in range(5):
            status = test_client.get("/queue/status").json()
            assert status["queue_size"] == 0
            time.sleep(0.5)

        assert job.result() == 3
