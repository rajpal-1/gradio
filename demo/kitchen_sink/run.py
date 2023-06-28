import gradio as gr
import os
os.environ['SYSTEM'] = "spaces"
os.environ['SPACE_ID'] = "aliabid94/audiotest100"


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            text = gr.Textbox()
            num = gr.Slider()
            radio = gr.Radio(["a", "b", "c"], value="a")
            file = gr.File()
            btn = gr.Button("Run")
        with gr.Column():
            img = gr.Image(shareable=["Prompt: ", text, "; seed:", num])
            audio = gr.Audio()
            video = gr.Video()
            gallery = gr.Gallery()
            chatbot = gr.Chatbot()

    btn.click(
        lambda *args: [
            "files/lion.jpg",
            "files/cantina.wav",
            "files/world.mp4",
            ["files/lion.jpg", "files/tower.jpg"],
            [["Hey", "I'm bot"], ["I'm human", "Ok"]],
        ],
        [text, num, radio, file],
        [img, audio, video, gallery, chatbot],
    )

if __name__ == "__main__":
    demo.launch()