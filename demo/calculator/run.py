import gradio as gr
from foo import foo_fn

if gr.NO_RELOAD:
    print("FOO")
    import numpy as np



def calculator(num1, operation, num2):
    print("foo_fn", foo_fn())
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise gr.Error("Cannot divide by zero!")
        return num1 / num2

demo = gr.Interface(
    calculator,
    [
        "number", 
        gr.Radio(["add", "subtract", "multiply", "divide"], label="OPeration@@"),
        "number"
    ],
    "number",
    examples=[
        [45, "add", 30],
        [3.14, "divide", 2],
        [144, "multiply", 2.5],
        [0, "subtract", 1.2],
    ],
    title="Toy Calculator",
    description="Here's a sample toy calculator. Allows you to calculate things like $2+2=4$",
)

if __name__ == "__main__":
    demo.launch()
