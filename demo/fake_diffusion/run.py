import gradio as gr
import numpy as np
import time

# define core fn, which returns a generator {steps} times before returning the image
def fake_diffusion(steps):
    for _ in range(steps):
        time.sleep(1)
        image = np.random.random((600, 600, 3))
        yield image
    image = "https://fastly.picsum.photos/id/237/600/600.jpg?hmac=KGSiyZ1y0xEcvk6vZQwzHW4bpTWEoXsMnRK6qbyBSAU"
    yield image


demo = gr.Interface(fake_diffusion, inputs=gr.Slider(1, 10, 3), outputs="image")

# define queue - required for generators
demo.queue()

demo.launch()
