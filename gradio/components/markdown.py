"""gr.Markdown() component."""

from __future__ import annotations

import inspect
import warnings
from typing import Any, Callable, Literal

from gradio_client.documentation import document, set_documentation_group

from gradio.components.base import Component, _Keywords
from gradio.events import Events

set_documentation_group("component")


@document()
class Markdown(Component):
    """
    Used to render arbitrary Markdown output. Can also render latex enclosed by dollar signs.
    Preprocessing: this component does *not* accept input.
    Postprocessing: expects a valid {str} that can be rendered as Markdown.

    Demos: blocks_hello, blocks_kinematics
    Guides: key-features
    """

    EVENTS = [Events.change]

    def __init__(
        self,
        value: str | Callable = "",
        *,
        rtl: bool = False,
        latex_delimiters: list[dict[str, str | bool]] | None = None,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        sanitize_html: bool = True,
        line_breaks: bool = False,
        **kwargs,
    ):
        """
        Parameters:
            value: Value to show in Markdown component. If callable, the function will be called whenever the app loads to set the initial value of the component.
            rtl: If True, sets the direction of the rendered text to right-to-left. Default is False, which renders text left-to-right.
            latex_delimiters: A list of dicts of the form {"left": open delimiter (str), "right": close delimiter (str), "display": whether to display in newline (bool)} that will be used to render LaTeX expressions. If not provided, `latex_delimiters` is set to `[{ "left": "$", "right": "$", "display": False }]`, so only expressions enclosed in $ delimiters will be rendered as LaTeX, and in the same line. Pass in an empty list to disable LaTeX rendering. For more information, see the [KaTeX documentation](https://katex.org/docs/autorender.html).
            visible: If False, component will be hidden.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.
            sanitize_html: If False, will disable HTML sanitization when converted from markdown. This is not recommended, as it can lead to security vulnerabilities.
            line_breaks: If True, will enable Github-flavored Markdown line breaks in chatbot messages. If False (default), single new lines will be ignored.
        """
        self.rtl = rtl
        self.latex_delimiters = latex_delimiters
        self.sanitize_html = sanitize_html
        self.line_breaks = line_breaks

        super().__init__(
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            value=value,
            **kwargs,
        )

    def postprocess(self, y: str | None) -> str | None:
        """
        Parameters:
            y: markdown representation
        Returns:
            HTML rendering of markdown
        """
        if y is None:
            return None
        unindented_y = inspect.cleandoc(y)
        return unindented_y

    def as_example(self, input_data: str | None) -> str:
        postprocessed = self.postprocess(input_data)
        return postprocessed if postprocessed else ""

    def preprocess(self, x: Any) -> Any:
        return x

    def example_inputs(self) -> Any:
        return "# Hello!"

    def api_info(self) -> dict[str, Any]:
        return {"type": "string"}
