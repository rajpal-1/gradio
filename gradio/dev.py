# Contains the function that runs when `gradio` is called from the command line. Specifically, allows
# $ gradio app.py to run app.py in development mode where any changes reload the script.

import os
import sys
from gradio import networking

def main():
    args = sys.argv[1:]
    
    path = args[0]
    path = os.path.normpath(path)
    if not(path == os.path.basename(path)):
        raise ValueError("Must provide file name in the current directory")
    filename = os.path.splitext(path)[0]   

    port = networking.get_first_available_port(
        networking.INITIAL_PORT_VALUE, 
        networking.INITIAL_PORT_VALUE + networking.TRY_NUM_PORTS
    )
    
    os.system(f"uvicorn {filename}:demo.app --reload --port {port}")

