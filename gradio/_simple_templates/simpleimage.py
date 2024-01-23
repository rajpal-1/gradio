from __future__ import annotations

from pathlib import Path
from typing import Any, Callable

from gradio.components.base import Component
from gradio.data_classes import FileData
from gradio.events import Events


class SimpleImage(Component):
    """
    Creates a very simple image for user to drag-and-drop or upload their image and get a preview, or display a static image.
    Preprocessing: passes the uploaded image as a {str} filepath.
    Postprocessing: expects a {str} or {pathlib.Path} filepath or URL to an image.
    Examples-format: expects a {str} or {pathlib.Path} filepath or URL to an image.
    """

    EVENTS = [
        Events.change,
        Events.input,
        Events.upload,
    ]

    def __init__(
        self,
        value: str | Callable | None = None,
        *,
        label: str | None = None,
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
            value: A path or URL for the default value that Image component is going to take. If callable, the function will be called whenever the app loads to set the initial value of the component.
            label: The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.
            every: If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. Queue must be enabled. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.
            show_label: if True, will display label.
            container: If True, will place the component in a container - providing some extra padding around the border.
            scale: relative width compared to adjacent Components in a Row. For example, if Component A has scale=2, and Component B has scale=1, A will be twice as wide as B. Should be an integer.
            min_width: minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.
            interactive: if True, will allow users to upload and edit an image; if False, can only be used to display images. If not provided, this is inferred based on whether the component is used as an input or output.
            visible: If False, component will be hidden.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.
            render: If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.
        """
        super().__init__(
            label=label,
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

    def preprocess(self, payload: FileData | None) ->  str | None:
        """
        Preprocesses image by converting it to a str before passing it to the function.
        Parameters:
            payload: an object containing the image data of type {FileData}.
        Returns:
            str path to a temporary file containing the image.
        """
        if payload is None:
            return None
        return payload.path

    def postprocess(self, value: str | Path | None) -> FileData | None:
        """
        Postprocesses image by converting it to a FileData object that can be displayed by the frontend.
        Parameters:
            value: a {str} or {pathlib.Path} to the image.
        Returns:
            a {FileData} object containing the image data.
        """
        if value is None:
            return None
        return FileData(path=str(value))

    def example_inputs(self) -> Any:
        return "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png"
