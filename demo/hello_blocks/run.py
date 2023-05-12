import gradio as gr
import time


def greet(name):
    time.sleep(1)
    raise ValueError()
    return "Hello " + name + "!"


with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(
        fn=greet, inputs=name, outputs=output
    )


if __name__ == "__main__":
    demo.launch()
