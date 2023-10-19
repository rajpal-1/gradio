import json
import os

DIR = os.path.dirname(__file__)
GRADIO_DEMO_DIR = os.path.abspath(os.path.join(DIR, "../../../../../demo/"))

def get_code_description_and_reqs(demo_name):
    with open(os.path.join(GRADIO_DEMO_DIR, demo_name, "run.py")) as f:
        code = f.read()
    description = ""
    if os.path.exists(os.path.join(GRADIO_DEMO_DIR, demo_name, "DESCRIPTION.md")):
        with open(os.path.join(GRADIO_DEMO_DIR, demo_name, "DESCRIPTION.md")) as f:
            description = f.read()
    requirements = []
    if os.path.exists(os.path.join(GRADIO_DEMO_DIR, demo_name, "requirements.txt")):
        with open(os.path.join(GRADIO_DEMO_DIR, demo_name, "requirements.txt")) as f:
            requirements = f.read().strip().split("\n")
    return code, description, requirements


demos_by_category = [
    {
        "category": "Text",
        "demos": [
            {
                "name": "Hello", 
                "dir": "hello_world", 
            },
            {
                "name": "Blocks", 
                "dir": "hello_blocks", 
            },
            {
                "name": "Sentences", 
                "dir": "sentence_builder", 
            },
            {
                "name": "Differ", 
                "dir": "diff_texts", 
            },
            

        ]
    },
     {
        "category": "Media",
        "demos": [
            {
                "name": "Filter", 
                "dir": "sepia_filter", 
            },
            {
                "name": "Identity",
                "dir": "video_identity_2",
            },
            {
                "name": "Webcam",
                "dir": "webcam",
            },
            {
                "name": "Iteration",
                "dir": "fake_diffusion",
            },
            {
                "name": "Tones", 
                "dir": "generate_tone", 
            },
            {
                "name": "Reverse", 
                "dir": "reverse_audio_2", 
            },
        ]
    },
    {
        "category": "Tabular",
        "demos": [
            {
                "name": "Records",
                "dir": "filter_records"
            },
            {
                "name": "Matrix",
                "dir": "matrix_transpose"
            },
            {
                "name": "Calculator",
                "dir": "tax_calculator"
            },
            {
                "name": "Kinematics", 
                "dir": "blocks_kinematics", 
            },
            {
                "name": "Forecast", 
                "dir": "stock_forecast", 
            },
        ]
    },
    {
        "category": "Other",
        "demos": [
            {
                "name": "Double", 
                "dir": "tabbed_interface_lite", 
            },
            {
                "name": "Chatbot", 
                "dir": "chatinterface_random_response", 
            },
            {
                "name": "Streaming", 
                "dir": "chatinterface_streaming_echo", 
            },
            {
                "name": "Layouts", 
                "dir": "blocks_flipper", 
            },
            {
                "name": "Error", 
                "dir": "calculator", 
            },
            {
                "name": "Chained", 
                "dir": "blocks_chained_events", 
            },
            {
                "name": "Changes", 
                "dir": "blocks_hello", 
            }
        ]
    }
]

for category in demos_by_category:
    for demo in category["demos"]:
        code, description, requirements = get_code_description_and_reqs(demo["dir"])
        demo["code"] = code
        demo["text"] = description
        demo["requirements"] = requirements 

def generate(json_path):
    with open(json_path, 'w+') as f:
        json.dump(demos_by_category, f)
