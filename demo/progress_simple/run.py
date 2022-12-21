import gradio as gr
import time

def reverse(word, progress=gr.Progress()):
    progress(0, desc="Starting")
    time.sleep(1)
    new_string = ""
    for letter in progress.track(word, desc="Reversing"):
        time.sleep(0.25)
        new_string = letter + new_string
    return new_string

demo = gr.Interface(reverse, gr.Text(), gr.Text())

if __name__ == "__main__":
    demo.queue(concurrency_count=10).launch()
