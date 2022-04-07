# Defines the Context class, which is used to store the state of all Blocks that are being rendered.

from __future__ import annotations

from typing import TYPE_CHECKING, List

if TYPE_CHECKING:  # Only import for type checking (is False at runtime).
    from gradio.blocks import Block


class Context:
    root_block: Block = None  # The current root block that holds all blocks.
    block: Block = None  # The current block that all children should be added to.
    id = 0  # Running id to uniquely refer to any block that gets defined
