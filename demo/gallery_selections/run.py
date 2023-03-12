import gradio as gr
import numpy as np

with gr.Blocks() as demo:
    num_images = gr.Dropdown(
        ["1", "2", "3", "4", "5", "6", "7", "8", "9"], value="6", label="Num Images"
    )
    
    with gr.Row(variant="panel"):
        text = gr.Textbox(
            show_label=False,
            max_lines=1,
            placeholder="Enter your prompt",
        ).style(
            container=False,
        )
        btn = gr.Button("Generate image").style(full_width=False)

    imgs = gr.State()
    gallery = gr.Gallery().style(preview=True)

    with gr.Row():
        selected = gr.Textbox(show_label=False, placeholder="Selected")
        darken_btn = gr.Button("Darken selected")

    def generate_images():
        images = []
        for i in range(9):
            color = np.random.randint(0, 255, 3)
            # create image with single color
            image = np.ones((100, 100, 3), dtype=np.uint8) * color
            images.append(image)
        return images, images

    btn.click(generate_images, None, [gallery, imgs])

    def get_select_index(evt: gr.SelectEvent):
        return evt.index

    gallery.select(get_select_index, None, selected)

    def darken_img(imgs, index):
        index = int(index)
        imgs[index] = np.round(imgs[index] * 0.8).astype(np.uint8)
        return imgs

    darken_btn.click(darken_img, [imgs, selected], gallery)

if __name__ == "__main__":
    demo.launch()
