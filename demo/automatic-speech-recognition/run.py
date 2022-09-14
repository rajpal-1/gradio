# URL: https://huggingface.co/spaces/gradio/automatic-speech-recognition
# DESCRIPTION: Automatic speech recognition in Chinese and English. Uses a tabbed layout to give the user the choice between uploading audio or recording from a microphone.
# imports
import gradio as gr
import os

# save your HF API token from https:/hf.co/settings/tokens as an env variable to avoid rate limiting
auth_token = os.getenv("auth_token")

# automatically load the interface from a HF model 
# you can remove the api_key parameter if you don't care about rate limiting. 
demo = gr.Interface.load(
    "huggingface/facebook/wav2vec2-base-960h",
    title="Speech-to-text",
    inputs="mic",
    description="Let me try to guess what you're saying!",
    api_key=auth_token
)

# launch
demo.launch()
