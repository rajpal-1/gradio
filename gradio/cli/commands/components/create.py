import shutil
from pathlib import Path
from typing import Optional

import typer
from rich import print
from rich.panel import Panel
from rich.prompt import Confirm, Prompt
from tomlkit import dump, parse
from typing_extensions import Annotated

from gradio.cli.commands.components.install_component import _get_npm, _install_command
from gradio.cli.commands.display import LivePanelDisplay

from . import _create_utils


def _create(
    name: Annotated[
        str,
        typer.Argument(
            help="Name of the component. Preferably in camel case, i.e. MyTextBox."
        ),
    ],
    directory: Annotated[
        Optional[Path],
        typer.Option(
            help="Directory to create the component in. Default is None. If None, will be created in <component-name> directory in the current directory."
        ),
    ] = None,
    package_name: Annotated[
        Optional[str],
        typer.Option(help="Name of the package. Default is gradio_{name.lower()}"),
    ] = None,
    template: Annotated[
        str,
        typer.Option(
            help="Component to use as a template. Should use exact name of python class."
        ),
    ] = "",
    install: Annotated[
        bool,
        typer.Option(
            help="Whether to install the component in your current environment as a development install. Recommended for development."
        ),
    ] = True,
    npm_install: Annotated[
        str,
        typer.Option(help="NPM install command to use. Default is 'npm install'."),
    ] = "npm install",
    overwrite: Annotated[
        bool,
        typer.Option(help="Whether to overwrite the existing component if it exists."),
    ] = False,
    configure_metadata: Annotated[
        bool,
        typer.Option(
            help="Whether to interactively configure project metadata based on user input"
        ),
    ] = True,
):
    if not directory:
        directory = Path(name.lower())
    if not package_name:
        package_name = f"gradio_{name.lower()}"

    if directory.exists() and not overwrite:
        raise ValueError(
            f"The directory {directory.resolve()} already exists. "
            "Please set --overwrite flag or pass in the name "
            "of a directory that does not already exist via the --directory option."
        )
    elif directory.exists() and overwrite:
        _create_utils.delete_contents(directory)

    directory.mkdir(exist_ok=overwrite)

    if _create_utils._in_test_dir():
        npm_install = f"{shutil.which('pnpm')} i --ignore-scripts"
    else:
        npm_install = _get_npm(npm_install)

    with LivePanelDisplay() as live:
        live.update(
            f":building_construction:  Creating component [orange3]{name}[/] in directory [orange3]{directory}[/]",
            add_sleep=0.2,
        )
        if template:
            live.update(f":fax: Starting from template [orange3]{template}[/]")
        else:
            live.update(":page_facing_up: Creating a new component from scratch.")

        component = _create_utils._get_component_code(template)

        _create_utils._create_backend(name, component, directory, package_name)
        live.update(":snake: Created backend code", add_sleep=0.2)

        _create_utils._create_frontend(
            name.lower(), component, directory=directory, package_name=package_name
        )
        live.update(":art: Created frontend code", add_sleep=0.2)

        if install:
            _install_command(directory, live, npm_install)

        live._panel.stop()

        if configure_metadata:
            print(
                Panel(
                    "It is recommended to answer the following [bold][magenta]4 questions[/][/] to finish configuring your custom component's metadata."
                    "\nYou can also answer them later by editing the [bold][magenta]pyproject.toml[/][/] file in your component directory."
                )
            )

            answer_qs = Confirm.ask("\nDo you want to answer them now?")

            if answer_qs:
                pyproject_toml = parse((directory / "pyproject.toml").read_text())
                name = pyproject_toml["project"]["name"]  # type: ignore

                description = Prompt.ask(
                    "\n:pencil: Please enter a one sentence [bold][magenta]description[/][/] for your component"
                )
                if description:
                    pyproject_toml["project"]["description"] = description  # type: ignore

                license_ = Prompt.ask(
                    "\n:bookmark_tabs: Please enter a [bold][magenta]software license[/][/] for your component. Leave blank for 'MIT'"
                )
                license_ = license_ or "MIT"
                print(f":bookmark_tabs: Using license [bold][magenta]{license_}[/][/]")
                pyproject_toml["project"]["license"] = license_  # type: ignore

                requires_python = Prompt.ask(
                    "\n:snake: Please enter the [bold][magenta]allowed python[/][/] versions for your component. Leave blank for '>=3.8'"
                )
                requires_python = requires_python or ">=3.8"
                print(
                    f":snake: Using requires-python of [bold][magenta]{requires_python}[/][/]"
                )
                pyproject_toml["project"]["requires-python"] = (
                    requires_python or ">=3.8"
                )  # type: ignore

                keywords = []
                print(
                    "\n:label: Please add some keywords to help others discover your component."
                )
                while True:
                    keyword = Prompt.ask(":label: Leave blank to stop adding keywords")
                    if keyword:
                        keywords.append(keyword)
                    else:
                        break
                current_keywords = pyproject_toml["project"].get("keywords", [])  # type: ignore
                pyproject_toml["project"]["keywords"] = current_keywords + keywords  # type: ignore
                with open(directory / "pyproject.toml", "w") as f:
                    dump(pyproject_toml, f)
                print("\nComponent creation [bold][magenta]complete[/][/]!")
