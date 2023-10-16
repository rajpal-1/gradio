import shutil
import subprocess
from pathlib import Path

import typer
from rich import print
from typing_extensions import Annotated

import gradio

gradio_template_path = Path(gradio.__file__).parent / "templates" / "frontend"
gradio_node_path = Path(gradio.__file__).parent / "node" / "dev" / "files" / "index.js"


def _dev(
    app: Annotated[
        Path,
        typer.Argument(
            help="The path to the app. By default, looks for demo/app.py in the current directory."
        ),
    ] = Path("demo")
    / "app.py",
    component_directory: Annotated[
        Path,
        typer.Option(
            help="The directory with the custom component source code. By default, uses the current directory."
        ),
    ] = Path("."),
    host: Annotated[
        str,
        typer.Option(
            help="The host to run the front end server on. Defaults to localhost.",
        ),
    ] = "localhost",
):
    component_directory = component_directory.resolve()

    print(f":recycle: [green]Launching[/] {app} in reload mode\n")

    node = shutil.which("node")
    if not node:
        raise ValueError("node must be installed in order to run dev mode.")

    proc = subprocess.Popen(
        [
            node,
            gradio_node_path,
            "--component-directory",
            component_directory,
            "--root",
            gradio_template_path,
            "--app",
            str(app),
            "--mode",
            "dev",
            "--host",
            host,
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    while True:
        proc.poll()
        text = proc.stdout.readline()  # type: ignore
        err = proc.stderr.readline()  # type: ignore

        text = (
            text.decode("utf-8")
            .replace("Changes detected in:", "[orange3]Changed detected in:[/]")
            .replace("Watching:", "[orange3]Watching:[/]")
            .replace("Running on local URL", "[orange3]Backend Server[/]")
        )

        if "[orange3]Watching:[/]" in text:
            text += f"'{str(component_directory / 'frontend').strip()}',"
        if "To create a public link" in text:
            continue
        print(text)
        print(err.decode("utf-8"))

        if proc.returncode is not None:
            print("Backend server failed to launch. Exiting.")
            return
