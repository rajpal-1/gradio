"""gr.ColorPicker() component."""

from __future__ import annotations

from typing import Any, Callable

from gradio_client.documentation import document

from gradio.components.base import Component
from gradio.events import Events


@document()
class ColorPicker(Component):
    """
    Creates a color picker for user to select a color as string input. Can be used as an input to pass a color value to a function or as an output to display a color value.
    Demos: color_picker, color_generator
    """

    EVENTS = [Events.change, Events.input, Events.submit, Events.focus, Events.blur]

    def __init__(
        self,
        value: str | Callable | None = None,
        *,
        label: str | None = None,
        info: str | None = None,
        every: float | None = None,
        show_label: bool | None = None,
        container: bool = True,
        scale: int | None = None,
        min_width: int = 160,
        interactive: bool | None = None,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        render: bool = True,
    ):
        """
        Parameters:
            value: default text to provide in color picker. If callable, the function will be called whenever the app loads to set the initial value of the component.
            label: The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.
            info: additional component description.
            every: If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise.sed (e.g. to cancel it) via this component's .load_event attribute.
            show_label: if True, will display label.
            container: If True, will place the component in a container - providing some extra padding around the border.
            scale: relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.
            min_width: minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.
            interactive: if True, will be rendered as an editable color picker; if False, editing will be disabled. If not provided, this is inferred based on whether the component is used as an input or output.
            visible: If False, component will be hidden.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.
            render: If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.
        """
        super().__init__(
            label=label,
            info=info,
            every=every,
            show_label=show_label,
            container=container,
            scale=scale,
            min_width=min_width,
            interactive=interactive,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            render=render,
            value=value,
        )

    def example_inputs(self) -> str:
        return "#000000"

    def api_info(self) -> dict[str, Any]:
        return {"type": "string"}

    def preprocess(self, payload: str | None) -> str | None:
        """
        Parameters:
            payload: Color as hex string
        Returns:
            Passes selected color value as a hex `str` into the function.
        """
        if payload is None:
            return None
        else:
            return str(payload)

    def postprocess(self, value: str | None) -> str | None:
        """
        Parameters:
            value: Expects a hex `str` returned from function and sets color picker value to it.
        Returns:
            A `str` value that is set as the color picker value.
        """
        if value is None:
            return None
        else:
            return str(value)
