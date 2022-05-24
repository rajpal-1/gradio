# Contains the function that runs when `gradio` is called from the command line. Specifically, allows
# $ gradio app.py to run app.py in development mode where any changes reload the script.

import os
import sys

from gradio import networking


def user():
    args = sys.argv[1:]
    if len(args) == 0:
        raise ValueError("No file specified.")
    if len(args) == 1:
        demo_name = "demo"
    else:
        demo_name = args[1]

    path = args[0]
    path = path.replace("/", ".")
    filename = os.path.splitext(path)[0]

    port = networking.get_first_available_port(
        networking.INITIAL_PORT_VALUE,
        networking.INITIAL_PORT_VALUE + networking.TRY_NUM_PORTS,
    )

    print(
        f"\nLaunching in *reload mode* on: http://{networking.LOCALHOST_NAME}:{port} (Press CTRL+C to quit)\n"
    )
    os.system(
        f"uvicorn {filename}:{demo_name}.app --reload --port {port} --log-level warning"
    )


def dev():
    args = sys.argv[1:]
    if len(args) == 0:
        raise ValueError("No file specified.")
    if len(args) == 1:
        demo_name = "demo"
    else:
        demo_name = args[1]

    path = args[0]
    path = path.replace("/", ".")
    filename = os.path.splitext(path)[0]
    port = networking.get_first_available_port(
        networking.INITIAL_PORT_VALUE,
        networking.INITIAL_PORT_VALUE + networking.TRY_NUM_PORTS,
    )

    print(
        f"\nLaunching in *developer reload mode* on: http://{networking.LOCALHOST_NAME}:{port} (Press CTRL+C to quit)\n"
    )
    os.system(
        f"uvicorn {filename}:{demo_name}.app --reload --port {port} --log-level warning --reload-dir gradio"
    )
