import json

import gradio._simple_templates
import gradio.image_utils
import gradio.processing_utils
import gradio.templates
from gradio import components, layouts, themes
from gradio.blocks import Blocks
from gradio.chat_interface import ChatInterface
from gradio.cli import deploy
from gradio.components import (
    HTML,
    JSON,
    AnnotatedImage,
    Annotatedimage,
    Audio,
    BarPlot,
    Button,
    Chatbot,
    Checkbox,
    CheckboxGroup,
    Checkboxgroup,
    ClearButton,
    Code,
    ColorPicker,
    DataFrame,
    Dataframe,
    Dataset,
    DownloadButton,
    Dropdown,
    DuplicateButton,
    File,
    FileExplorer,
    Gallery,
    Highlight,
    HighlightedText,
    Highlightedtext,
    Image,
    ImageEditor,
    Json,
    Label,
    LinePlot,
    LoginButton,
    LogoutButton,
    Markdown,
    Model3D,
    Number,
    ParamViewer,
    Plot,
    Radio,
    ScatterPlot,
    Slider,
    State,
    Text,
    Textbox,
    UploadButton,
    Video,
    component,
)
from gradio.components.audio import WaveformOptions
from gradio.components.image_editor import Brush, Eraser
from gradio.data_classes import FileData
from gradio.events import EventData, KeyUpData, LikeData, SelectData, on
from gradio.exceptions import Error
from gradio.external import load
from gradio.flagging import (
    CSVLogger,
    FlaggingCallback,
    HuggingFaceDatasetSaver,
    SimpleCSVLogger,
)
from gradio.helpers import (
    Info,
    Progress,
    Warning,
    make_waveform,
    skip,
    update,
)
from gradio.helpers import create_examples as Examples  # noqa: N812
from gradio.interface import Interface, TabbedInterface, close_all
from gradio.ipython_ext import load_ipython_extension
from gradio.layouts import Accordion, Column, Group, Row, Tab, TabItem, Tabs
from gradio.oauth import OAuthProfile, OAuthToken
from gradio.routes import Request, mount_gradio_app
from gradio.templates import (
    Files,
    ImageMask,
    List,
    Matrix,
    Mic,
    Microphone,
    Numpy,
    Paint,
    PlayableVideo,
    Sketchpad,
    TextArea,
)
from gradio.themes import Base as Theme
from gradio.utils import get_package_version, set_static_paths, no_reload

__version__ = get_package_version()
