import gradio as gr

with gr.Blocks() as demo:
    gr.LoginButton()

demo.launch()
