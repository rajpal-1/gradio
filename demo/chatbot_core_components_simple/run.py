import gradio as gr
import random

# Chatbot demo with multimodal input (text, markdown, LaTeX, code blocks, image, audio, & video). Plus shows support for streaming text.

color_map = {
    "harmful": "crimson",
    "neutral": "gray",
    "beneficial": "green",
}

def html_src(harm_level):
    return f"""
<div style="display: flex; gap: 5px;">
  <div style="background-color: {color_map[harm_level]}; padding: 2px; border-radius: 5px;">
  {harm_level}
  </div>
</div>
"""

def print_like_dislike(x: gr.LikeData):
    print(x.index, x.value, x.liked)

def add_message(history, message):
    for x in message["files"]:
        history.append(((x,), None))
    if message["text"] is not None:
        history.append((message["text"], None))
    return history, gr.MultimodalTextbox(value=None, interactive=False)

def bot(history, response_type):
    if response_type == "gallery":
        history[-1][1] = gr.Gallery(
            [
                "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",
                "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",
            ]
        )
    elif response_type == "image":
        history[-1][1] = gr.Image(
            "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png"
        )
    elif response_type == "video":
        history[-1][1] = gr.Video(
            "https://github.com/gradio-app/gradio/raw/main/demo/video_component/files/world.mp4"
        )
    elif response_type == "audio":
        history[-1][1] = gr.Audio(
            "https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav"
        )
    elif response_type == "html":
        history[-1][1] = gr.HTML(
            html_src(random.choice(["harmful", "neutral", "beneficial"]))
        )
    else:
        history[-1][1] = "Cool!"
    return history

with gr.Blocks(fill_height=True) as demo:
    chatbot = gr.Chatbot(
        elem_id="chatbot",
        bubble_full_width=False,
        scale=1,
    )
    response_type = gr.Radio(
        [
            "image",
            "text",
            "gallery",
            "video",
            "audio",
            "html",
        ],
        value="text",
        label="Response Type",
    )

    chat_input = gr.MultimodalTextbox(
        interactive=True,
        placeholder="Enter message or upload file...",
        show_label=False,
    )

    chat_msg = chat_input.submit(
        add_message, [chatbot, chat_input], [chatbot, chat_input]
    )
    bot_msg = chat_msg.then(
        bot, [chatbot, response_type], chatbot, api_name="bot_response"
    )
    bot_msg.then(lambda: gr.MultimodalTextbox(interactive=True), None, [chat_input])

    chatbot.like(print_like_dislike, None, None)

if __name__ == "__main__":
    demo.launch()
