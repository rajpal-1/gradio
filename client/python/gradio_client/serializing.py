from __future__ import annotations

import json
import os
import uuid
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List, Tuple

from gradio_client import utils


class Serializable(ABC):
    @abstractmethod
    def api_info(self) -> Dict[str, Tuple[str, str]]:
        """
        The typing information for this component as a dictionary whose values are (Python type, language-agnostic description) tuples.
        Keys of the dictionary are: raw_input, raw_output, serialized_input, serialized_output
        """
        pass

    def serialize(self, x: Any, load_dir: str | Path = ""):
        """
        Convert data from human-readable format to serialized format for a browser.
        """
        return x

    def deserialize(
        self,
        x: Any,
        save_dir: str | Path | None = None,
        root_url: str | None = None,
        hf_token: str | None = None,
    ):
        """
        Convert data from serialized format for a browser to human-readable format.
        """
        return x


class SimpleSerializable(Serializable):
    """General class that does not perform any serialization or deserialization."""

    def api_info(self) -> Dict[str, Tuple[str, str]]:
        return {
            "raw_input": ("Any", ""),
            "raw_output": ("Any", ""),
            "serialized_input": ("Any", ""),
            "serialized_output": ("Any", ""),
        }


class StringSerializable(Serializable):
    """Expects a string as input/output but performs no serialization."""

    def api_info(self) -> Dict[str, Tuple[str, str]]:
        return {
            "raw_input": ("str", "string value"),
            "raw_output": ("str", "string value"),
            "serialized_input": ("str", "string value"),
            "serialized_output": ("str", "string value"),
        }


class ListStringSerializable(Serializable):
    """Expects a list of strings as input/output but performs no serialization."""

    def api_info(self) -> Dict[str, Tuple[str, str]]:
        return {
            "raw_input": ("List[str]", "list of string values"),
            "raw_output": ("List[str]", "list of string values"),
            "serialized_input": ("List[str]", "list of string values"),
            "serialized_output": ("List[str]", "list of string values"),
        }


class BooleanSerializable(Serializable):
    """Expects a boolean as input/output but performs no serialization."""

    def api_info(self) -> Dict[str, Tuple[str, str]]:
        return {
            "raw_input": ("bool", "boolean value"),
            "raw_output": ("bool", "boolean value"),
            "serialized_input": ("bool", "boolean value"),
            "serialized_output": ("bool", "boolean value"),
        }


class NumberSerializable(Serializable):
    """Expects a number (int/float) as input/output but performs no serialization."""

    def api_info(self) -> Dict[str, Tuple[str, str]]:
        return {
            "raw_input": ("int | float", "numeric value"),
            "raw_output": ("int | float", "numeric value"),
            "serialized_input": ("int | float", "numeric value"),
            "serialized_output": ("int | float", "numeric value"),
        }


class ImgSerializable(Serializable):
    """Expects a base64 string as input/output which is serialized to a filepath."""

    def api_info(self) -> Dict[str, Tuple[str, str]]:
        return {
            "raw_input": ("str", "base64 representation of image"),
            "raw_output": ("str", "base64 representation of image"),
            "serialized_input": ("str", "filepath or URL to image"),
            "serialized_output": ("str", "filepath or URL to image"),
        }

    def serialize(
        self,
        x: str | None,
        load_dir: str | Path = "",
    ) -> str | None:
        """
        Convert from human-friendly version of a file (string filepath) to a seralized
        representation (base64).
        Parameters:
            x: String path to file to serialize
            load_dir: Path to directory containing x
        """
        if x is None or x == "":
            return None
        is_url = utils.is_valid_url(x)
        path = x if is_url else Path(load_dir) / x
        return utils.encode_url_or_file_to_base64(path)

    def deserialize(
        self,
        x: str | None,
        save_dir: str | Path | None = None,
        root_url: str | None = None,
        hf_token: str | None = None,
    ) -> str | None:
        """
        Convert from serialized representation of a file (base64) to a human-friendly
        version (string filepath). Optionally, save the file to the directory specified by save_dir
        Parameters:
            x: Base64 representation of image to deserialize into a string filepath
            save_dir: Path to directory to save the deserialized image to
            root_url: Ignored
            hf_token: Ignored
        """
        if x is None or x == "":
            return None
        file = utils.decode_base64_to_file(x, dir=save_dir)
        return file.name


class FileSerializable(Serializable):
    """Expects a dict with base64 representation of object as input/output which is serialized to a filepath."""

    def api_info(self) -> Dict[str, Tuple[str, str]]:
        return {
            "raw_input": (
                "str | Dict",
                "base64 string representation of file; or a dictionary-like object, the keys should be either: is_file (False), data (base64 representation of file) or is_file (True), name (str filename)",
            ),
            "raw_output": (
                "Dict",
                "dictionary-like object with keys: name (str filename), data (base64 representation of file), is_file (bool, set to False)",
            ),
            "serialized_input": ("str", "filepath or URL to file"),
            "serialized_output": ("str", "filepath or URL to file"),
        }

    def serialize(
        self,
        x: str | None,
        load_dir: str | Path = "",
    ) -> Dict | None:
        """
        Convert from human-friendly version of a file (string filepath) to a
        seralized representation (base64)
        Parameters:
            x: String path to file to serialize
            load_dir: Path to directory containing x
        """
        if x is None or x == "":
            return None
        if utils.is_valid_url(x):
            filename = x
        else:
            filename = str(Path(load_dir) / x)
        return {
            "name": filename,
            "data": utils.encode_url_or_file_to_base64(filename),
            "orig_name": Path(filename).name,
            "is_file": False,
        }

    def deserialize(
        self,
        x: str | Dict | None,
        save_dir: Path | str | None = None,
        root_url: str | None = None,
        hf_token: str | None = None,
    ) -> str | None:
        """
        Convert from serialized representation of a file (base64) to a human-friendly
        version (string filepath). Optionally, save the file to the directory specified by `save_dir`
        Parameters:
            x: Base64 representation of file to deserialize into a string filepath
            save_dir: Path to directory to save the deserialized file to
            root_url: If this component is loaded from an external Space, this is the URL of the Space.
            hf_token: If this component is loaded from an external private Space, this is the access token for the Space
        """
        if x is None:
            return None
        if isinstance(save_dir, Path):
            save_dir = str(save_dir)
        if isinstance(x, str):
            file_name = utils.decode_base64_to_file(x, dir=save_dir).name
        elif isinstance(x, dict):
            if x.get("is_file"):
                if root_url is not None:
                    file_name = utils.download_tmp_copy_of_file(
                        root_url + "file=" + x["name"],
                        hf_token=hf_token,
                        dir=save_dir,
                    ).name
                else:
                    file_name = utils.create_tmp_copy_of_file(
                        x["name"], dir=save_dir
                    ).name
            else:
                file_name = utils.decode_base64_to_file(x["data"], dir=save_dir).name
        else:
            raise ValueError(
                f"A FileSerializable component can only deserialize a string or a dict, not a: {type(x)}"
            )
        return file_name


class JSONSerializable(Serializable):
    def api_info(self) -> Dict[str, Tuple[str, str]]:
        return {
            "raw_input": ("str | Dict | List", "JSON-serializable object or a string"),
            "raw_output": ("Dict | List", "dictionary- or list-like object"),
            "serialized_input": ("str", "filepath to JSON file"),
            "serialized_output": ("str", "filepath to JSON file"),
        }

    def serialize(
        self,
        x: str | None,
        load_dir: str | Path = "",
    ) -> Dict | List | None:
        """
        Convert from a a human-friendly version (string path to json file) to a
        serialized representation (json string)
        Parameters:
            x: String path to json file to read to get json string
            load_dir: Path to directory containing x
        """
        if x is None or x == "":
            return None
        return utils.file_to_json(Path(load_dir) / x)

    def deserialize(
        self,
        x: str | Dict | List,
        save_dir: str | Path | None = None,
        root_url: str | None = None,
        hf_token: str | None = None,
    ) -> str | None:
        """
        Convert from serialized representation (json string) to a human-friendly
        version (string path to json file).  Optionally, save the file to the directory specified by `save_dir`
        Parameters:
            x: Json string
            save_dir: Path to save the deserialized json file to
            root_url: Ignored
            hf_token: Ignored
        """
        if x is None:
            return None
        return utils.dict_or_str_to_json_file(x, dir=save_dir).name


class GallerySerializable(Serializable):
    def input_api_info(self) -> Tuple[str, str]:
        return "str", "path to directory with images and captions.json"

    def output_api_info(self) -> Tuple[str, str]:
        return "str", "path to directory with images and captions.json"

    def serialize(
        self, x: str | None, load_dir: str | Path = ""
    ) -> List[List[str]] | None:
        if x is None or x == "":
            return None
        files = []
        captions_file = Path(x) / "captions.json"
        with captions_file.open("r") as captions_json:
            captions = json.load(captions_json)
        for file_name, caption in captions.items():
            img = FileSerializable().serialize(file_name)
            files.append([img, caption])
        return files

    def deserialize(
        self,
        x: Any,
        save_dir: str = "",
        root_url: str | None = None,
        hf_token: str | None = None,
    ) -> None | str:
        if x is None:
            return None
        gallery_path = Path(save_dir) / str(uuid.uuid4())
        gallery_path.mkdir(exist_ok=True, parents=True)
        captions = {}
        for img_data in x:
            if isinstance(img_data, list) or isinstance(img_data, tuple):
                img_data, caption = img_data
            else:
                caption = None
            name = FileSerializable().deserialize(
                img_data, gallery_path, root_url=root_url, hf_token=hf_token
            )
            captions[name] = caption
            captions_file = gallery_path / "captions.json"
            with captions_file.open("w") as captions_json:
                json.dump(captions, captions_json)
        return os.path.abspath(gallery_path)


SERIALIZER_MAPPING = {cls.__name__: cls for cls in Serializable.__subclasses__()}
SERIALIZER_MAPPING["Serializable"] = SimpleSerializable

COMPONENT_MAPPING: Dict[str, type] = {
    "textbox": StringSerializable,
    "number": NumberSerializable,
    "slider": NumberSerializable,
    "checkbox": BooleanSerializable,
    "checkboxgroup": ListStringSerializable,
    "radio": StringSerializable,
    "dropdown": SimpleSerializable,
    "image": ImgSerializable,
    "video": FileSerializable,
    "audio": FileSerializable,
    "file": FileSerializable,
    "dataframe": JSONSerializable,
    "timeseries": JSONSerializable,
    "state": SimpleSerializable,
    "button": StringSerializable,
    "uploadbutton": FileSerializable,
    "colorpicker": StringSerializable,
    "label": JSONSerializable,
    "highlightedtext": JSONSerializable,
    "json": JSONSerializable,
    "html": StringSerializable,
    "gallery": GallerySerializable,
    "chatbot": JSONSerializable,
    "model3d": FileSerializable,
    "plot": JSONSerializable,
    "markdown": StringSerializable,
    "dataset": StringSerializable,
    "code": StringSerializable,
}
