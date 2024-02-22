import gradio as gr
import os
import time

# Chatbot demo with multimodal input (text, markdown, LaTeX, code blocks, image, audio, & video). Plus shows support for streaming text.


def print_like_dislike(x: gr.LikeData):
    print(x.index, x.value, x.liked)

def add_message(history, message):
    for x in message:
        if x["type"] == "file" and x["file"]["path"] is not None:  
            history.append(((x["file"]["path"],), None))  
        elif x["type"] == "text" and x["text"] is not None:
            history.append((x["text"], None))
    return history, gr.MultimodalTextbox(value=[], interactive=False)

def bot(history):
    response = "**That's cool!**"
    history[-1][1] = ""
    for character in response:
        history[-1][1] += character
        time.sleep(0.05)
        yield history


with gr.Blocks() as demo:
    chatbot = gr.Chatbot(
        [],
        elem_id="chatbot",
        bubble_full_width=False,
        avatar_images=(None, (os.path.join(os.path.dirname(__file__), "avatar.png"))),
    )

    chat_input = gr.MultimodalTextbox(label="Name", interactive=True, placeholder="Enter message or upload file...")
    chat_msg = chat_input.submit(add_message, [chatbot, chat_input], [chatbot, chat_input], queue=False).then(
        bot, chatbot, chatbot, api_name="bot_response"
    )
    chat_msg.then(lambda: gr.Textbox(interactive=True), None, [chat_input], queue=False)
    chatbot.like(print_like_dislike, None, None)

demo.queue()
if __name__ == "__main__":
    demo.launch()
