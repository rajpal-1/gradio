import os.path
import gradio as gr


def load_mesh(mesh_file_name):
    return mesh_file_name

iface = gr.Interface(
    fn=load_mesh,
    inputs=gr.inputs.Image3D(),
    outputs=gr.outputs.Image3D(clear_color=[0.8, 0.2, 0.2, 1.0]),
    examples=[["files/Bunny.obj"], ["files/Duck.glb"]]
)

if __name__ == "__main__":
    iface.launch()
