# import gradio as gr
# from pathlib import Path


# dir_ = Path(__file__).parent


# def predict(im):
#     return im


# with gr.Blocks() as demo:
#     with gr.Row():
#         im = gr.ImageEditor(
#             type="numpy",
#             interactive=True,
#         )
#         im_preview = gr.ImageEditor(
#             interactive=True,
#         )

#     set_background = gr.Button("Set Background")
#     set_background.click(
#         lambda: {
#             "background": str(dir_ / "cheetah.jpg"),
#             "layers": None,
#             "composite": None,
#         },
#         None,
#         im,
#         show_progress="hidden",
#     )
#     set_layers = gr.Button("Set Layers")
#     set_layers.click(
#         lambda: {
#             "background": str(dir_ / "cheetah.jpg"),
#             "layers": [str(dir_ / "layer1.png")],
#             "composite": None,
#         },
#         None,
#         im,
#         show_progress="hidden",
#     )
#     set_composite = gr.Button("Set Composite")
#     set_composite.click(
#         lambda: {
#             "background": None,
#             "layers": None,
#             "composite": "https://nationalzoo.si.edu/sites/default/files/animals/cheetah-003.jpg",
#         },
#         None,
#         im,
#         show_progress="hidden",
#     )

#     im.change(
#         predict,
#         outputs=im_preview,
#         inputs=im,
#     )

#     gr.Examples(
#         examples=[
#             "https://upload.wikimedia.org/wikipedia/commons/0/09/TheCheethcat.jpg",
#             {
#                 "background": str(dir_ / "cheetah.jpg"),
#                 "layers": [str(dir_ / "layer1.png")],
#                 "composite": None,
#             },
#         ],
#         inputs=im,
#     )


# if __name__ == "__main__":
#     demo.launch()

import gradio as gr


def fn(im):
    im["composite"]  # the full canvas
    im["background"]  # the background image
    im["layers"]  # a list of individual layers


with gr.Blocks() as demo:
    im = gr.ImageEditor(
        # decide which sources you'd like to accept
        sources=["upload", "webcam", "clipboard"],
        # set a cropsize constraint, can either be a ratio or a concrete [width, height]
        crop_size="1:1",
        # enable crop (or disable it)
        transforms=["crop"],
        # customise the brush
    )

if __name__ == "__main__":
    demo.launch()
