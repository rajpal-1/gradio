[![CircleCI](https://circleci.com/gh/gradio-app/gradio.svg?style=svg)](https://circleci.com/gh/gradio-app/gradio)  [![PyPI version](https://badge.fury.io/py/gradio.svg)](https://badge.fury.io/py/gradio)  [![codecov](https://codecov.io/gh/gradio-app/gradio/branch/master/graph/badge.svg?token=NNVPX9KEGS)](https://codecov.io/gh/gradio-app/gradio) [![PyPI - Downloads](https://img.shields.io/pypi/dm/gradio)](https://pypi.org/project/gradio/) [![Twitter Follow](https://img.shields.io/twitter/follow/gradio.svg?style=social&label=Follow)](https://twitter.com/gradio)

#  Welcome to Gradio

Quickly create beautiful user interfaces around your machine learning models. Gradio (pronounced GRAY-dee-oh) makes it easy for you to demo your model in your browser or let people "try it out" by dragging-and-dropping in their own images, pasting text, recording their own voice, etc. and seeing what the model outputs.  

![Interface montage](website/homepage/src/assets/img/montage.gif)

Gradio is useful for:

* **Demoing** your machine learning models for clients / collaborators / users / students

* **Deploying** your models quickly with automatic shareable links and getting feedback on model performance

* **Debugging** your model interactively during development using built-in manipulation and interpretation tools

**You can find an interactive version of the following Getting Started at [https://gradio.app/getting_started](https://gradio.app/getting_started).**


## Getting Started

**Prerequisite**: Python 3.7+ and that's it! 

### Quick Start

To get Gradio running with a simple "Hello, World" example, follow these three steps:

<span>1.</span> Install Gradio from pip.

```bash
pip install gradio
```

<span>2.</span> Run the code below as a Python script or in a Python notebook (or in a  [colab notebook](https://colab.research.google.com/drive/18ODkJvyxHutTN0P5APWyGFO_xwNcgHDZ?usp=sharing)).

```python
import gradio as gr


def greet(name):
    return "Hello " + name + "!!"


iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()

```

<span>3.</span> The interface below will appear automatically within the Python notebook, or pop in a browser on  [http://localhost:7860](http://localhost:7860/)  if running from a script.

![hello_world interface](demo/hello_world/screenshot.gif)

### Understanding the `Interface` class

Gradio can wrap almost any Python function with an easy-to-use user interface. In the example above, we saw a simple text-based function. But the function could be anything from image enhancer to a tax calculator to (most commonly) the prediction function of a pretrained machine learning model.

The core  `Interface`  class is initialized with three parameters:

-   `fn`: the function to wrap
-   `inputs`: the input component type(s), e.g. `"image"` or `"audio"` ([see docs for complete list](/docs))
-   `outputs`: the output component type(s) e.g. `"image"` or `"label"` ([see docs for complete list](/docs))

With these three arguments, we can quickly create interfaces and  `launch()`  them. But what if you want to change how the UI components look or behave?

### Customizable Components

Let's say we want to customize the input text field - for example, we wanted it to be larger and have a text hint. If we use the actual input class for  `Textbox`  instead of using the string shortcut, we have access to much more customizability. To see a list of all the components we support and how you can customize them, check out the [Docs](https://gradio.app/docs).

```python
import gradio as gr


def greet(name):
    return "Hello " + name + "!"


iface = gr.Interface(
    fn=greet,
    inputs=gr.inputs.Textbox(lines=2, placeholder="Name Here..."),
    outputs="text",
)
iface.launch()

```
![hello_world_2 interface](demo/hello_world_2/screenshot.gif)

### Multiple Inputs and Outputs

Let's say we had a much more complex function, with multiple inputs and outputs. In the example below, we have a function that takes a string, boolean, and number, and returns a string and number. Take a look how we pass a list of input and output components.

```python
import gradio as gr


def greet(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = "%s %s. It is %s degrees today" % (salutation, name, temperature)
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)


iface = gr.Interface(
    fn=greet,
    inputs=["text", "checkbox", gr.inputs.Slider(0, 100)],
    outputs=["text", "number"],
)
iface.launch()

```
![hello_world_3 interface](demo/hello_world_3/screenshot.gif)

We simply wrap the components in a list. Each component in the `inputs` list corresponds to one of the parameters of the function, in order. Each component in the `outputs` list corresponds to one of the values returned by the function, again in order. 

### Working with Images

Let's try an image-to-image function. When using the  `Image`  component, your function will receive a numpy array of your specified size, with the shape  `(width, height, 3)`, where the last dimension represents the RGB values. We'll return an image as well in the form of a numpy array.

```python
import numpy as np

import gradio as gr


def sepia(input_img):
    sepia_filter = np.array(
        [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]
    )
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()
    return sepia_img


iface = gr.Interface(sepia, gr.inputs.Image(shape=(200, 200)), "image")

iface.launch()

```
![sepia_filter interface](demo/sepia_filter/screenshot.gif)

Additionally, our  `Image`  input interface comes with an 'edit' button which opens tools for cropping, flipping, rotating, drawing over, and applying filters to images. We've found that manipulating images in this way will often reveal hidden flaws in a model.

In addition to images, Gradio supports other media input types, such as audio or video uploads, as well as many output components. Read about these in the [Docs](https://gradio.app/docs).

### Working with DataFrames and Graphs

You can use Gradio to support inputs and outputs from your typical data libraries, such as numpy arrays, pandas dataframes, and plotly graphs. Take a look at the demo below (ignore the complicated data manipulation in the function!)

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import gradio as gr


def sales_projections(employee_data):
    sales_data = employee_data.iloc[:, 1:4].astype("int").to_numpy()
    regression_values = np.apply_along_axis(
        lambda row: np.array(np.poly1d(np.polyfit([0, 1, 2], row, 2))), 0, sales_data
    )
    projected_months = np.repeat(
        np.expand_dims(np.arange(3, 12), 0), len(sales_data), axis=0
    )
    projected_values = np.array(
        [
            month * month * regression[0] + month * regression[1] + regression[2]
            for month, regression in zip(projected_months, regression_values)
        ]
    )
    plt.plot(projected_values.T)
    plt.legend(employee_data["Name"])
    return employee_data, plt.gcf(), regression_values


iface = gr.Interface(
    sales_projections,
    gr.inputs.Dataframe(
        headers=["Name", "Jan Sales", "Feb Sales", "Mar Sales"],
        default=[["Jon", 12, 14, 18], ["Alice", 14, 17, 2], ["Sana", 8, 9.5, 12]],
    ),
    ["dataframe", "plot", "numpy"],
    description="Enter sales figures for employees to predict sales trajectory over year.",
)
iface.launch()

```
![sales_projections interface](demo/sales_projections/screenshot.gif)

### Example Inputs

You can provide example data that a user can easily load into the model. This can be helpful to demonstrate the types of inputs the model expects, as well as to provide a way to explore your dataset in conjunction with your model. To load example data, you provide a **nested list** to the  `examples=`  keyword argument of the Interface constructor. Each sublist within the outer list represents a data sample, and each element within the sublist represents an input for each input component. The format of example data for each component is specified in the  [Docs](https://gradio.app/docs).

```python
import gradio as gr


def calculator(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2


iface = gr.Interface(
    calculator,
    ["number", gr.inputs.Radio(["add", "subtract", "multiply", "divide"]), "number"],
    "number",
    examples=[
        [5, "add", 3],
        [4, "divide", 2],
        [-4, "multiply", 2.5],
        [0, "subtract", 1.2],
    ],
    title="test calculator",
    description="heres a sample toy calculator. enjoy!",
    flagging_options=["this", "or", "that"],
)

iface.launch()

```
![calculator interface](demo/calculator/screenshot.gif)

You can load a large dataset into the examples to browse and interact with the dataset through Gradio. The examples will be automatically paginated (you can configure this through the `examples_per_page` argument of Interface) and you can use CTRL + arrow keys to navigate through the examples quickly.

### Live Interfaces

You can make interfaces automatically refresh by setting `live=True` in the interface. Now the interface will recalculate as soon as the user input changes.

```python
import gradio as gr


def calculator(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2


iface = gr.Interface(
    calculator,
    ["number", gr.inputs.Radio(["add", "subtract", "multiply", "divide"]), "number"],
    "number",
    live=True,
)

iface.launch()

```
![calculator_live interface](demo/calculator_live/screenshot.gif)

Note there is no submit button, because the interface resubmits automatically on change.

### Using State

Your function may use data that persists beyond a single function call. If the data is something accessible to all function calls and all users, you can create a global variable outside the function call and access it inside the function. For example, you may load a large model outside the function and use it inside the function so that every function call does not need to reload the model.

Another type of data persistence Gradio supports is session **state**, where data persists across multiple submits within a page load. However, data is *not* shared between different users of your model. To store data in a session state, you need to do three things: (1) Pass in an extra parameter into your function, which represents the state of the interface. (2) At the end of the function, return the updated value of the state as an extra return value (3) Add the `'state'` input and `'state'` output components when creating your `Interface`. See the chatbot example below: 

```python
import random

import gradio as gr


def chat(message, history):
    history = history or []
    if message.startswith("How many"):
        response = random.randint(1, 10)
    elif message.startswith("How"):
        response = random.choice(["Great", "Good", "Okay", "Bad"])
    elif message.startswith("Where"):
        response = random.choice(["Here", "There", "Somewhere"])
    else:
        response = "I don't know"
    history.append((message, response))
    html = "<div class='chatbot'>"
    for user_msg, resp_msg in history:
        html += f"<div class='user_msg'>{user_msg}</div>"
        html += f"<div class='resp_msg'>{resp_msg}</div>"
    html += "</div>"
    return html, history


iface = gr.Interface(
    chat,
    ["text", "state"],
    ["html", "state"],
    css="""
    .chatbox {display:flex;flex-direction:column}
    .user_msg, .resp_msg {padding:4px;margin-bottom:4px;border-radius:4px;width:80%}
    .user_msg {background-color:cornflowerblue;color:white;align-self:start}
    .resp_msg {background-color:lightgray;align-self:self-end}
""",
    allow_screenshot=False,
    allow_flagging="never",
)
iface.launch()

```
![chatbot interface](demo/chatbot/screenshot.gif)

Notice how the state persists across submits within each page, but the state is not shared between the two pages. Some more points to note: you can pass in a default value to the state parameter, which is used as the initial value of the state. The state must be a something that can be serialized to a JSON format (e.g. a dictionary, a list, or a single value. Typically, objects will not work).  

### Flagging

Underneath the output interfaces, there is a button marked "Flag". When a user testing your model sees input with interesting output, such as erroneous or unexpected model behaviour, they can flag the input for the interface creator to review. Within the directory provided by the  `flagging_dir=`  argument to the Interface constructor, a CSV file will log the flagged inputs. If the interface involves file data, such as for Image and Audio components, folders will be created to store those flagged data as well.

For example, with the calculator interface shown above, we would have the flagged data stored in the flagged directory shown below:

```directory
+-- calculator.py
+-- flagged/
|   +-- logs.csv
```

*flagged/logs.csv*
```csv
num1,operation,num2,Output
5,add,7,12
6,subtract,1.5,4.5
```

With the sepia interface shown above, we would have the flagged data stored in the flagged directory shown below:

```directory
+-- sepia.py
+-- flagged/
|   +-- logs.csv
|   +-- im/
|   |   +-- 0.png
|   |   +-- 1.png
|   +-- Output/
|   |   +-- 0.png
|   |   +-- 1.png
```

*flagged/logs.csv*
```csv
im,Output
im/0.png,Output/0.png
im/1.png,Output/1.png
```

You can review these flagged inputs by manually exploring the flagging directory, or load them into the examples of the Gradio interface by pointing the  `examples=`  argument to the flagged directory. If you wish for the user to provide a reason for flagging, you can pass a list of strings to the `flagging_options` argument of Interface. Users will have to select one of the strings when flagging, which will be saved as an additional column to the CSV.

### Sharing Interfaces Publicly

Interfaces can be easily shared publicly by setting `share=True` in the `launch()` method. Like this:

```python
gr.Interface(classify_image, "image", "label").launch(share=True)
```

This generates a public, shareable link that you can send to anybody! When you send this link, the user on the other side can try out the model in their browser. Because the processing happens on your device (as long as your device stays on!), you don't have to worry about any packaging any dependencies. If you're working out of colab notebook, a share link is always automatically created. It usually looks something like this:  **XXXXX.gradio.app**. Although the link is served through a gradio link, we are only a proxy for your local server, and do not store any data sent through the interfaces.

Keep in mind, however, that these links are publicly accessible, meaning that anyone can use your model for prediction! Therefore, make sure not to expose any sensitive information through the functions you write, or allow any critical changes to occur on your device. If you set `share=False` (the default), only a local link is created, which can be shared by  [port-forwarding](https://www.ssh.com/ssh/tunneling/example)  with specific users. 

Share links expire after 72 hours. For permanent hosting, see Hosting Gradio Apps on Spaces below.

![Sharing diagram](website/homepage/src/assets/img/sharing.svg)

### Hosting Gradio Apps on Spaces

Huggingface provides the infrastructure to permanently host your Gradio model on the internet, for free! You can either drag and drop a folder containing your Gradio model and all related files, or you can point HF Spaces to your Git repository and HP Spaces will pull the Gradio interface from there. See [Huggingface Spaces](http://huggingface.co/spaces/) for more information. 

![Hosting Demo](website/homepage/src/assets/img/hf_demo.gif)

## Advanced Features
<span id="advanced-features"></span>

Here, we go through several advanced functionalities that your Gradio demo can include without you needing to write much more code!

### Authentication

You may wish to put an authentication page in front of your interface to limit who can open your interface. With the `auth=` keyword argument in the `launch()` method, you can pass a list of acceptable username/password tuples; or, for more complex authentication handling, you can even pass a function that takes a username and password as arguments, and returns True to allow authentication, False otherwise. Here's an example that provides password-based authentication for a single user named "admin":

```python
gr.Interface(fn=classify_image, inputs=image, outputs=label).launch(auth=("admin", "pass1234"))
```

### Interpreting your Predictions

Most models are black boxes such that the internal logic of the function is hidden from the end user. To encourage transparency, we've made it very easy to add interpretation to your model by  simply setting the `interpretation` keyword in the `Interface` class to `default`. This allows your users to understand what parts of the input are responsible for the output. Take a look at the simple interface below which shows an image classifier that also includes interpretation:

```python
import requests
import tensorflow as tf

import gradio as gr

inception_net = tf.keras.applications.MobileNetV2()  # load the model

# Download human-readable labels for ImageNet.
response = requests.get("https://git.io/JJkYN")
labels = response.text.split("\n")


def classify_image(inp):
    inp = inp.reshape((-1, 224, 224, 3))
    inp = tf.keras.applications.mobilenet_v2.preprocess_input(inp)
    prediction = inception_net.predict(inp).flatten()
    return {labels[i]: float(prediction[i]) for i in range(1000)}


image = gr.inputs.Image(shape=(224, 224))
label = gr.outputs.Label(num_top_classes=3)

gr.Interface(
    fn=classify_image, inputs=image, outputs=label, interpretation="default"
).launch()

```


In addition to `default`, Gradio also includes [Shapley-based interpretation](https://christophm.github.io/interpretable-ml-book/shap.html), which provides more accurate interpretations, albeit usually with a slower runtime. To use this, simply set the `interpretation` parameter to `"shap"` (note: also make sure the python package `shap` is installed). Optionally, you can modify the the `num_shap` parameter, which controls the tradeoff between accuracy and runtime (increasing this value generally increases accuracy). Here is an example:

```python
gr.Interface(fn=classify_image, inputs=image, outputs=label, interpretation="shap", num_shap=5).launch()
```

This will work for any function, even if internally, the model is a complex neural network or some other black box. If you use Gradio's `default` or `shap` interpretation, the output component must be a `Label`. All common input components are supported. Here is an example with text input.

```python
import re

import gradio as gr

male_words, female_words = ["he", "his", "him"], ["she", "hers", "her"]


def gender_of_sentence(sentence):
    male_count = len([word for word in sentence.split() if word.lower() in male_words])
    female_count = len(
        [word for word in sentence.split() if word.lower() in female_words]
    )
    total = max(male_count + female_count, 1)
    return {"male": male_count / total, "female": female_count / total}


iface = gr.Interface(
    fn=gender_of_sentence,
    inputs=gr.inputs.Textbox(default="She went to his house to get her keys."),
    outputs="label",
    interpretation="default",
)
iface.launch()

```

So what is happening under the hood? With these interpretation methods, Gradio runs the prediction multiple times with modified versions of the input. Based on the results, you'll see that the interface automatically highlights the parts of the text (or image, etc.) that contributed increased the likelihood of the class as red. The intensity of color corresponds to the importance of that part of the input. The parts that decrease the class confidence are highlighted blue.

You can also write your own interpretation function. The demo below adds custom interpretation to the previous demo. This function will take the same inputs as the main wrapped function. The output of this interpretation function will be used to highlight the input of each input interface - therefore the number of outputs here corresponds to the number of input interfaces. To see the format for interpretation for each input interface, check the Docs.

```python
import re

import gradio as gr

male_words, female_words = ["he", "his", "him"], ["she", "hers", "her"]


def gender_of_sentence(sentence):
    male_count = len([word for word in sentence.split() if word.lower() in male_words])
    female_count = len(
        [word for word in sentence.split() if word.lower() in female_words]
    )
    total = max(male_count + female_count, 1)
    return {"male": male_count / total, "female": female_count / total}


def interpret_gender(sentence):
    result = gender_of_sentence(sentence)
    is_male = result["male"] > result["female"]
    interpretation = []
    for word in re.split("( )", sentence):
        score = 0
        token = word.lower()
        if (is_male and token in male_words) or (not is_male and token in female_words):
            score = 1
        elif (is_male and token in female_words) or (
            not is_male and token in male_words
        ):
            score = -1
        interpretation.append((word, score))
    return interpretation


iface = gr.Interface(
    fn=gender_of_sentence,
    inputs=gr.inputs.Textbox(default="She went to his house to get her keys."),
    outputs="label",
    interpretation=interpret_gender,
    enable_queue=True,
)
iface.launch()

```

### Themes and Custom Styling

If you'd like to change how your interface looks, you can select a different theme by simply passing in the `theme` parameter, like so:

```python
gr.Interface(fn=classify_image, inputs=image, outputs=label, theme="huggingface").launch()
```

Here are the themes we currently support: `"default"`, `"huggingface"`, `"grass"`, `"peach"`, and the dark themes corresponding to each of these: `"darkdefault"`, `"darkhuggingface"`, `"darkgrass"`, `"darkpeach"`.

If you'd like to have more fine-grained control over any aspect of the app, you can also write your own css or pass in a css file, with the `css` parameter of the `Interface` class.

### Custom Flagging Options

In some cases, you might like to provide your users or testers with *more* than just a binary option to flag a sample. You can provide `flagging_options` that they select from a dropdown each time they click the flag button. This lets them provide additional feedback every time they flag a sample.

Here's an example:

```python
gr.Interface(fn=classify_image, inputs=image, outputs=label, flagging_options=["incorrect", "ambiguous", "offensive", "other"]).launch()
```

### Loading Hugging Face Models and Spaces

Gradio integrates nicely with the Hugging Face Hub, allowing you to load models and Spaces with just one line of code. To use this, simply use the `load()` method in the `Interface` class. So:

- To load any model from the Hugging Face Hub and create an interface around it, you pass `"model/"` or `"huggingface/"` followed by the model name, like these examples:

```python
gr.Interface.load("huggingface/gpt2").launch();
```

```python
gr.Interface.load("huggingface/EleutherAI/gpt-j-6B", 
    inputs=gr.inputs.Textbox(lines=5, label="Input Text")  # customizes the input component
).launch()
```

- To load any Space from the Hugging Face Hub and recreate it locally (so that you can customize the inputs and outputs for example), you pass `"spaces/"` followed by the model name:

```python
gr.Interface.load("spaces/eugenesiow/remove-bg", inputs="webcam", title="Remove your webcam background!").launch()
```

One of the great things about loading Hugging Face models or spaces using Gradio is that you can then immediately use the resulting `Interface` object just like function in your Python code (this works for every type of model/space: text, images, audio, video, and even multimodal models):

```python
io = gr.Interface.load("models/EleutherAI/gpt-neo-2.7B")
io("It was the best of times")  # outputs model completion
```

### Putting Interfaces in Parallel and Series

Gradio also lets you mix interfaces very easily using the `gradio.Parallel` and `gradio.Series` classes. `Parallel` lets you put two similar models (if they have the same input type) in parallel to compare model predictions:

```python
generator1 = gr.Interface.load("huggingface/gpt2")
generator2 = gr.Interface.load("huggingface/EleutherAI/gpt-neo-2.7B")
generator3 = gr.Interface.load("huggingface/EleutherAI/gpt-j-6B")

gr.Parallel(generator1, generator2, generator3).launch()
```

`Series` lets you put models and spaces in series, piping the output of one model into the input of the next model. 

```python
generator = gr.Interface.load("huggingface/gpt2")
translator = gr.Interface.load("huggingface/t5-small")

gr.Series(generator, translator).launch()  # this demo generates text, then translates it to German, and outputs the final result.
```

And of course, you can also mix `Parallel` and `Series` together whenever that makes sense!

### Queuing to Manage Long Inference Times

If many people are using your interface or if the inference time of your function is long (> 1min), simply set the `enable_queue` parameter in the `launch` method to `True` to prevent timeouts.

```python
gr.Interface(fn=classify_image, inputs=image, outputs=label).launch(enable_queue=True)
```

This sets up a queue of workers to handle the predictions and return the response to the front end. This is strongly recommended if you are planning on uploading your demo to Hugging Face Spaces (as described above) so that you can manage a large number of users simultaneously using your demo.





##  System Requirements:

Gradio requires Python `3.7+` and has been tested on the latest versions of Windows, MacOS, and various common Linux distributions (e.g. Ubuntu). For Python package requirements, please see the `setup.py` file.

##  Contributing:

If you would like to contribute and your contribution is small, you can directly open a pull request (PR). If you would like to contribute a larger feature, we recommend first creating an issue with a proposed design for discussion. Please see our [contributing guidelines](https://github.com/gradio-app/gradio/blob/master/CONTRIBUTING.md) for more info.

##  License:

Gradio is licensed under the Apache License 2.0


##  See more:

You can find many more examples as well as more info on usage on our website: www.gradio.app

See, also, the accompanying paper: ["Gradio: Hassle-Free Sharing and Testing of ML Models in the Wild"](https://arxiv.org/pdf/1906.02569.pdf), *ICML HILL 2019*, and please use the citation below.

```
@article{abid2019gradio,
title={Gradio: Hassle-Free Sharing and Testing of ML Models in the Wild},
author={Abid, Abubakar and Abdalla, Ali and Abid, Ali and Khan, Dawood and Alfozan, Abdulrahman and Zou, James},
journal={arXiv preprint arXiv:1906.02569},
year={2019}
}
```