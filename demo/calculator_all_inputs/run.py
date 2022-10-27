import gradio as gr

with gr.Blocks() as demo:
    a = gr.Number(label="a")
    b = gr.Number(label="b")
    with gr.Row():
        add_btn = gr.Button("Add")
        sub_btn = gr.Button("Subtract")
    c = gr.Number(label="sum")

    def add(data):
        data[c] = data[a] + data[b]
    add_btn.click(add, inputs="all")

    def sub(data):
        data[c] = data[a] - data[b]
    sub_btn.click(sub, inputs="all")

if __name__ == "__main__":
    demo.launch()