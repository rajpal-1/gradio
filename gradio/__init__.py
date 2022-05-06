import pkg_resources

import gradio.components as components
import gradio.inputs as inputs
import gradio.outputs as outputs
import gradio.processing_utils
from gradio.blocks import Blocks, Column, Row, TabItem, Tabs
from gradio.components import (
    HTML,
    JSON,
    Audio,
    Button,
    DataFrame,
    Keyvalues,
    Highlightedtext,
    Checkboxgroup,
    TimeSeries,
    Carousel,
    Chatbot,
    Checkbox,
    CheckboxGroup,
    Dataframe,
    Dropdown,
    File,
    Gallery,
    HighlightedText,
    Image,
    KeyValues,
    Label,
    Markdown,
    Model3D,
    Number,
    Plot,
    Radio,
    Slider,
    StatusTracker,
    Textbox,
    Timeseries,
    Variable,
    Video,
    component,
)
from gradio.flagging import (
    CSVLogger,
    FlaggingCallback,
    HuggingFaceDatasetSaver,
    SimpleCSVLogger,
)
from gradio.interface import Interface, TabbedInterface, close_all
from gradio.mix import Parallel, Series

current_pkg_version = pkg_resources.require("gradio")[0].version
__version__ = current_pkg_version
