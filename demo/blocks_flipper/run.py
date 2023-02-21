# import numpy as np
# import gradio as gr

# def flip_text(x):
#     return x[::-1]

# def flip_image(x):
#     return np.fliplr(x)

# with gr.Blocks() as demo:
#     gr.Markdown("Flip text or image files using this demo.")
#     with gr.Tab("Flip Text"):
#         text_input = gr.Textbox()
#         text_output = gr.Textbox()
#         text_button = gr.Button("Flip")
#     with gr.Tab("Flip Image"):
#         with gr.Row():
#             image_input = gr.Image()
#             image_output = gr.Image()
#         image_button = gr.Button("Flip")

#     with gr.Accordion("Open for More!"):
#         gr.Markdown("Look at me...")

#     text_button.click(flip_text, inputs=text_input, outputs=text_output)
#     image_button.click(flip_image, inputs=image_input, outputs=image_output)

# if __name__ == "__main__":
#     demo.launch()

import gradio as gr
from PIL import Image

img = Image.new("RGB", (512, 512), (0, 0, 0))
img.save("image.png", "PNG")

print(img)


def save_image(image):
    image.save("colorede.png")
    return image


with gr.Blocks() as demo:
    image = gr.Image(value="image.png", interactive=True, tool="color-sketch")
    button = gr.Button()
    button.click(save_image, inputs=image, outputs=[])

if __name__ == "__main__":
    demo.launch()
