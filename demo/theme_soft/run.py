import gradio as gr
import time

def repeat(name, count):
    time.sleep(3)
    return name * count

demo = gr.Interface(
    fn=repeat,
    inputs=[gr.Textbox(), gr.Slider(label="Count")],
    outputs=gr.Textbox(label="Output"),
    theme=gr.themes.Soft(),
)

if __name__ == "__main__":
    demo.launch()