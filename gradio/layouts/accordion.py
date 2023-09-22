from __future__ import annotations

import warnings
from typing import TYPE_CHECKING, Literal

from gradio_client.documentation import document, set_documentation_group

from gradio.blocks import BlockContext
from gradio.component_meta import ComponentMeta
from gradio.deprecation import warn_deprecation, warn_style_method_deprecation
from gradio.events import Events

if TYPE_CHECKING:
    from gradio.blocks import Block

set_documentation_group("layout")


@document()
class Accordion(BlockContext, metaclass=ComponentMeta):
    """
    Accordion is a layout element which can be toggled to show/hide the contained content.
    Example:
        with gr.Accordion("See Details"):
            gr.Markdown("lorem ipsum")
    """

    EVENTS = []

    def __init__(
        self,
        label,
        *,
        open: bool = True,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        **kwargs,
    ):
        """
        Parameters:
            label: name of accordion section.
            open: if True, accordion is open by default.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional string or list of strings that are assigned as the class of this component in the HTML DOM. Can be used for targeting CSS styles.
        """
        self.label = label
        self.open = open
        BlockContext.__init__(
            self, visible=visible, elem_id=elem_id, elem_classes=elem_classes, **kwargs
        )

    @staticmethod
    def update(
        open: bool | None = None,
        label: str | None = None,
        visible: bool | None = None,
    ):
        return {
            "visible": visible,
            "label": label,
            "open": open,
            "__type__": "update",
        }
