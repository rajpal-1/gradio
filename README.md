<!-- DO NOT EDIT THIS FILE DIRECTLY. INSTEAD EDIT THE `readme_template.md` OR `guides/1)getting_started/1)quickstart.md` TEMPLATES AND THEN RUN `render_readme.py` SCRIPT. -->

<div align="center">

[<img src="readme_files/gradio.svg" alt="gradio" width=400>](https://gradio.app)<br>

[![gradio-backend](https://github.com/gradio-app/gradio/actions/workflows/backend.yml/badge.svg)](https://github.com/gradio-app/gradio/actions/workflows/backend.yml)
[![gradio-ui](https://github.com/gradio-app/gradio/actions/workflows/ui.yml/badge.svg)](https://github.com/gradio-app/gradio/actions/workflows/ui.yml)  
 [![PyPI](https://img.shields.io/pypi/v/gradio)](https://pypi.org/project/gradio/)
[![PyPI downloads](https://img.shields.io/pypi/dm/gradio)](https://pypi.org/project/gradio/)
![Python version](https://img.shields.io/badge/python-3.8+-important)
[![Twitter follow](https://img.shields.io/twitter/follow/gradio?style=social&label=follow)](https://twitter.com/gradio)

[Website](https://gradio.app)
| [Documentation](https://gradio.app/docs/)
| [Guides](https://gradio.app/guides/)
| [Getting Started](https://gradio.app/getting_started/)
| [Examples](demo/)
| [中文](readme_files/zh-cn#readme)

</div>

# Gradio: Build Machine Learning Web Apps — in Python



Gradio is an open-source Python package that allows you to quickly **build** a demo or web application for your machine learning model, API, or any arbitary Python function. You can then **share** a link to your demo or web application in just a few seconds using Gradio's built-in sharing features. *No JavaScript, CSS, or web hosting experience needed!*

It just takes a few lines of Python to create a beautiful demo, so let's get started 💫

### Installation

**Prerequisite**: Gradio requires [Python 3.8 or higher](https://www.python.org/downloads/), that's all!


We recommend installing Gradio using `pip`, which is included by default in Python. Run this in your terminal or command prompt:

```bash
pip install gradio
```


✍️ **Tip:** it is best to install Gradio in a virtual environment. Detailed installation instructions for all common operating systems <a href="/guides/installing-gradio-in-a-virtual-environment">are provided here</a>. 

### Building Your First Demo

You can run Gradio in your favorite code editor, Jupyter notebook, [Google Colab](https://colab.research.google.com/drive/18ODkJvyxHutTN0P5APWyGFO_xwNcgHDZ?usp=sharing), or anywhere else you write Python. Let's write our first Gradio app:


```python
import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="textbox", outputs="textbox")
    
demo.launch()
```



✍️ **Tip:** We shorten the imported name from <code>gradio</code> to <code>gr</code> for better readability of code. This is a widely adopted convention that you should follow so that anyone working with your code can easily understand it. 

Now, run your code. If you've written the Python code in a file named, for example, `app.py`, then you would run `python app.py` from the terminal.

The demo below will open in a browser on [http://localhost:7860](http://localhost:7860) if running from a file. If you are running within a notebook, the demo will appear embedded within the notebook.

![`hello_world` demo](demo/hello_world/screenshot.gif)

Type your name in the textbox on the left, and then press the Submit button. You should see a friendly greeting on the right.

✍️ **Tip:** When developing locally, you can run your Gradio app in <strong>hot reload mode</strong>, which automatically reloads the Gradio app whenever you make changes to the file. To do this, simply type in <code>gradio</code> before the name of the file instead of <code>python</code>. In the example above, you would type: `gradio app.py` in your terminal. Learn more about hot reloading in the <a href="https://gradio.app/developing-faster-with-reload-mode/">Hot Reloading Guide</a>.


### Input/Output Demos: The `Interface` Class

You'll notice that in order to make your first demo, you created an instance of the `gr.Interface` class. The `Interface` class is designed to create demos for machine learning models which accept one or more inputs, and return one or more outputs. 

Despite its simplicity, the `Interface` class is very flexible -- it can wrap *any* Python function with a user interface (UI). In the example above, we saw a simple text-based function, but the function could be anything from music generator to a tax calculator to the prediction function of a pretrained machine learning model.

The core `Interface` class has three core arguments:

- `fn`: the function to wrap a UI around
- `inputs`: which Gradio component(s) to use for the input. The number of components should match the number of arguments in your function.
- `outputs`: which Gradio component(s) to use for the output. The number of components should match the number of return values from your function.


As we'll see, Gradio includes more than [30 built-in components](https://www.gradio.app/docs) (such as the `gr.Textbox()`, `gr.Image()`, `gr.HTML()`, and so on). For the `inputs` and `outputs` arguments, you must pass in the name of one of these components as a string, or an instance of the class. Passing in a class instance allows you to customize the properties of the your component (e.g. the number of lines in a `gr.Textbox()`). 

If your function accepts more than one argument, you can pass in a list of input components to `inputs`, with each input component corresponding to one of the arguments of the function, in order. The same holds true if your function returns more than one value: simply pass in a list of components to `outputs`. 

The following example shows how to use `gr.Interface` with multiple inputs and outputs:

```python
import gradio as gr

def greet(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}. It is {temperature} degrees today"
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "checkbox", gr.Slider(0, 100)],
    outputs=["text", "number"],
)
demo.launch()
```


![`hello_world_3` demo](demo/hello_world_3/screenshot.gif)


We dive deeper into the `gr.Interface` on our series on [building Interfaces](/guides/02_building-interfaces/01_interface-state.md).

### Chatbots: The `ChatInterface` Class

Gradio includes another high-level class, `gr.ChatInterface`, which is specifically designed to create Chatbot UIs.

The `gr.ChatInterface` class also wraps a function, but this function must have a specific signature. The function should take two arguments: `message` and then `history` (the arguments can be named anything, but must be in this order)

- `message`: a `str` representing the user's input
- `history`: a `list` of `list` representing the conversations up until that point. Each inner list consists of two `str` representing a pair: `[user input, bot response]`.

The function should return a single `str` response, which is the bot's response to the particular user input's `message`, and it can also take into account the `history` of messages so far.

Other than that, `ChatInterface` has no required arguments (though several are available for customization of the UI).

Here's a toy example showing how to use `ChatInterfae`:

```python
import random
import gradio as gr

def random_response(message, history):
    return random.choice(["Yes", "No"])

demo = gr.ChatInterface(random_response)

demo.launch()
```


![`chatinterface_random_response` demo](demo/chatinterface_random_response/screenshot.gif)

If you're interested in creating a chatbot, you can jump straight to `gr.ChatInterface` in [our dedicated guide](/guides/creating-a-chatbot-fast).

### Complex Demos: The `Blocks` Class

So far, we've discussed the **Interface** and **ChatInterface** classes, which provide high-level abstractions that let you very quickly create demos for input/output models and chatbots respectively. But what if your demo doesn't fall into one of these cases?

Gradio also includes a **Blocks** class, which offers a low-level approach for designing web apps with more flexible layouts and data flows. Blocks allows you to do things like control where components appear on the page, handle complex data flows (e.g. outputs can serve as inputs to other functions), and update properties/visibility of components based on user interaction — still all in Python. 

Let's take a look at a simple example, similar to our first `Interface` demo. Notice how the syntax here differs from `gr.Interface`.

```python
import gradio as gr

def greet(name):
    return "Hello " + name + "!"

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

demo.launch()
```


![`hello_blocks` demo](demo/hello_blocks/screenshot.gif)

Things to note:

- a `Blocks` demo starts with a `with` clause, and any component created inside this clause is automatically added to the app.
- Components appear vertically in the app in the order they are created. (Later, we will cover customizing layouts!)
- A `Button` was created, and then a `click()` event-listener was added to this button. The arguments for the `click()` event should look familiar! Like an `Interface`, the `click()` method takes a Python function, input components, and output components.

You can build very custom and complex applications using `gr.Blocks()`. For example, the popular image generation [Automatic1111 Web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) is built using Gradio Blocks.

We dive deeper into the `gr.Blocks` on our series on [building with Blocks](/guides/03_building-with-blocks/01_blocks-and-event-listeners.md).

### Sharing Your Demo

What good is a cool demo if you can't share it? Gradio lets you easily share a machine learning demo without having to worry about the hassle of hosting on a web server. Simply set `share=True` in `launch()`, and a publicly accessible URL will be created for your demo. To revisit our first example, notice the last line of code here:

```python
import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="textbox", outputs="textbox")
    
demo.launch(share=True) 
```

When you run this code, a public URL will be generated for your demo in a matter of seconds, something like:

👉 &nbsp; `https://a23dsf231adb.gradio.live`

Now, anyone around the world can use your Gradio application from their browser, while the machine learning model and all computation continues to run locally on your computer. Sharing a demo works this way whether you are launching an `Interface`, `ChatInterface`, or `Blocks`.

To learn more about sharing your demo, read our dedicated guide on [sharing your Gradio application](/guides/01_getting-started/03_sharing-your-app.md).

### The Gradio Ecosystem

So far, we've been discussing the core `gradio` Python library. But Gradio is actually so much more! Its an entire ecosystem of Python and JavaScript libraries that let you build machine learning applications, or query them via API, in Python or JavaScript. Here are other related parts of the Gradio ecosystem:

* [Gradio Python Client](/guides/08_client-libraries/01_getting-started-with-the-python-client.md) (`gradio_client`): the easiest way to query any Gradio app via an API from Python.
* [Gradio JavaScript Client](/guides/08_client-libraries/02_getting-started-with-the-js-client.md) (`@gradio/client`): the easiest way to query any Gradio app via an API from JavaScript.
* [Gradio-Lite](/guides/09_other-tutorials/gradio-lite.md) (`@gradio/lite`): write Gradio apps in Python that run entirely in the browser (no server needed!), thanks to Pyodide. 
* [Hugging Face Spaces](https://huggingface.co/spaces): the most popular place to host Gradio applications, supports CPU instances (for free 🤗) as well as GPU instances.

### What's Next?

Keep learning about Gradio sequentially through our conceptual guides, which include explanations as well as example code and embedded interactive demos. Next up: our series on [building Interfaces](/guides/02_building-interfaces/01_interface-state.md).

Or, if you already know the basics and are looking for something specific, you can search the more [technical API documentation](https://www.gradio.app/docs/).




## Questions?

If you'd like to report a bug or have a feature request, please create an [issue on GitHub](https://github.com/gradio-app/gradio/issues/new/choose). For general questions about usage, we are available on [our Discord server](https://discord.com/invite/feTf9x3ZSB) and happy to help.

If you like Gradio, please leave us a ⭐ on GitHub!

## Open Source Stack

Gradio is built on top of many wonderful open-source libraries!

[<img src="readme_files/huggingface_mini.svg" alt="huggingface" height=40>](https://huggingface.co)
[<img src="readme_files/python.svg" alt="python" height=40>](https://www.python.org)
[<img src="readme_files/fastapi.svg" alt="fastapi" height=40>](https://fastapi.tiangolo.com)
[<img src="readme_files/encode.svg" alt="encode" height=40>](https://www.encode.io)
[<img src="readme_files/svelte.svg" alt="svelte" height=40>](https://svelte.dev)
[<img src="readme_files/vite.svg" alt="vite" height=40>](https://vitejs.dev)
[<img src="readme_files/pnpm.svg" alt="pnpm" height=40>](https://pnpm.io)
[<img src="readme_files/tailwind.svg" alt="tailwind" height=40>](https://tailwindcss.com)
[<img src="readme_files/storybook.svg" alt="storybook" height=40>](https://storybook.js.org/)
[<img src="readme_files/chromatic.svg" alt="chromatic" height=40>](https://www.chromatic.com/)

## License

Gradio is licensed under the Apache License 2.0 found in the [LICENSE](LICENSE) file in the root directory of this repository.

## Citation

Also check out the paper _[Gradio: Hassle-Free Sharing and Testing of ML Models in the Wild](https://arxiv.org/abs/1906.02569), ICML HILL 2019_, and please cite it if you use Gradio in your work.

```
@article{abid2019gradio,
  title = {Gradio: Hassle-Free Sharing and Testing of ML Models in the Wild},
  author = {Abid, Abubakar and Abdalla, Ali and Abid, Ali and Khan, Dawood and Alfozan, Abdulrahman and Zou, James},
  journal = {arXiv preprint arXiv:1906.02569},
  year = {2019},
}
```
