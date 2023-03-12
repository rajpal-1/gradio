import gradio as gr

def add_text(history, text):
    history = history + [(text, text + "?")]
    return history

def add_file(history, file):
    history = history + [((file.name,), "Cool file!")]
    return history

def bot_response(history):
    if isinstance(history[-1][0], str):
        response = "Cool!"
    else:
        response = "Cool file!"
    history[-1][1] = response
    return history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(elem_id="chatbot").style(height=750)
    
    with gr.Row():
        with gr.Column(scale=0.85):
            txt = gr.Textbox(
                show_label=False,
                placeholder="Enter text and press enter, or upload an image",
            ).style(container=False)
        with gr.Column(scale=0.15, min_width=0):
            btn = gr.UploadButton("📁", file_types=["image", "video", "audio"])
            
    txt.submit(add_text, [chatbot, txt], [chatbot, txt]).then(
        bot_response, chatbot, chatbot
    )
    btn.upload(add_file, [chatbot, btn], [chatbot]).then(
        bot_response, chatbot, chatbot
    )

if __name__ == "__main__":
    demo.launch()
