
import gradio as gr
from gradio_test_four import test_four


with gr.Blocks() as demo:
    gr.Markdown("# Change the value (keep it JSON) and the front-end will update automatically.")
    test_four(value={"message": "Hello from Gradio!"}, label="Static")


if __name__ == "__main__":
    demo.launch()
