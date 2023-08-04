"""gr.ColorPicker() component."""

from __future__ import annotations

from typing import Any, Callable

from gradio_client.documentation import document, set_documentation_group
from gradio_client.serializing import StringSerializable

from gradio.blocks import Default
from gradio.components.base import IOComponent
from gradio.events import (
    Changeable,
    Focusable,
    Inputable,
    Submittable,
)

set_documentation_group("component")


@document()
class ColorPicker(
    Changeable, Inputable, Submittable, Focusable, IOComponent, StringSerializable
):
    """
    Creates a color picker for user to select a color as string input.
    Preprocessing: passes selected color value as a {str} into the function.
    Postprocessing: expects a {str} returned from function and sets color picker value to it.
    Examples-format: a {str} with a hexadecimal representation of a color, e.g. "#ff0000" for red.
    Demos: color_picker, color_generator
    """

    def __init__(
        self,
        value: str | Callable | None | Default = Default(None),
        *,
        label: str | None | Default = Default(None),
        info: str | None | Default = Default(None),
        every: float | None | Default = Default(None),
        show_label: bool | None | Default = Default(None),
        container: bool | None | Default = Default(True),
        scale: int | None | Default = Default(None),
        min_width: int | None | Default = Default(160),
        interactive: bool | None | Default = Default(None),
        visible: bool | Default = Default(True),
        elem_id: str | None | Default = Default(None),
        elem_classes: list[str] | str | None | Default = Default(None),
        **kwargs,
    ):
        """
        Parameters:
            value: default text to provide in color picker. If callable, the function will be called whenever the app loads to set the initial value of the component.
            label: component name in interface.
            info: additional component description.
            every: If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.
            show_label: if True, will display label.
            container: If True, will place the component in a container - providing some extra padding around the border.
            scale: relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.
            min_width: minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.
            interactive: if True, will be rendered as an editable color picker; if False, editing will be disabled. If not provided, this is inferred based on whether the component is used as an input or output.
            visible: If False, component will be hidden.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.
        """
        IOComponent.__init__(
            self,
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
            value=value,
            **kwargs,
        )

    def example_inputs(self) -> dict[str, Any]:
        return {
            "raw": "#000000",
            "serialized": "#000000",
        }

    def preprocess(self, x: str | None) -> str | None:
        """
        Any preprocessing needed to be performed on function input.
        Parameters:
            x: text
        Returns:
            text
        """
        if x is None:
            return None
        else:
            return str(x)

    def postprocess(self, y: str | None) -> str | None:
        """
        Any postprocessing needed to be performed on function output.
        Parameters:
            y: text
        Returns:
            text
        """
        if y is None:
            return None
        else:
            return str(y)
