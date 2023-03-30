XRAY_CONFIG = {
    "version": "3.23.1b3",
    "mode": "blocks",
    "dev_mode": True,
    "analytics_enabled": False,
    "components": [
        {
            "id": 1,
            "type": "markdown",
            "props": {
                "value": "<h1>Detect Disease From Scan</h1>\n<p>With this model you can lorem ipsum</p>\n<ul>\n<li>ipsum 1</li>\n<li>ipsum 2</li>\n</ul>\n",
                "name": "markdown",
                "visible": True,
                "style": {},
            },
            "serializer": "Serializable",
            "info": {"input": ["str", "value"], "output": ["str", "value"]},
        },
        {
            "id": 2,
            "type": "checkboxgroup",
            "props": {
                "choices": ["Covid", "Malaria", "Lung Cancer"],
                "value": [],
                "label": "Disease to Scan For",
                "show_label": True,
                "name": "checkboxgroup",
                "visible": True,
                "style": {},
            },
            "serializer": "Serializable",
            "info": {
                "input": ["List[str]", "values"],
                "output": ["List[str]", "values"],
            },
        },
        {"id": 3, "type": "tabs", "props": {"visible": True, "style": {}}},
        {
            "id": 4,
            "type": "tabitem",
            "props": {"label": "X-ray", "visible": True, "style": {}},
        },
        {
            "id": 5,
            "type": "row",
            "props": {
                "type": "row",
                "variant": "default",
                "visible": True,
                "style": {},
            },
        },
        {
            "id": 6,
            "type": "image",
            "props": {
                "image_mode": "RGB",
                "source": "upload",
                "tool": "editor",
                "streaming": False,
                "mirror_webcam": True,
                "show_label": True,
                "name": "image",
                "visible": True,
                "style": {},
            },
            "serializer": "ImgSerializable",
            "info": {
                "input": ["str", "filepath or URL"],
                "output": ["str", "filepath or URL"],
            },
        },
        {
            "id": 7,
            "type": "json",
            "props": {"show_label": True, "name": "json", "visible": True, "style": {}},
            "serializer": "JSONSerializable",
            "info": {
                "input": ["str", "filepath to json file"],
                "output": ["str", "filepath to json file"],
            },
        },
        {
            "id": 8,
            "type": "button",
            "props": {
                "value": "Run",
                "variant": "secondary",
                "interactive": True,
                "name": "button",
                "visible": True,
                "style": {},
            },
            "serializer": "Serializable",
            "info": {"input": ["str", "value"], "output": ["str", "value"]},
        },
        {
            "id": 9,
            "type": "tabitem",
            "props": {"label": "CT Scan", "visible": True, "style": {}},
        },
        {
            "id": 10,
            "type": "row",
            "props": {
                "type": "row",
                "variant": "default",
                "visible": True,
                "style": {},
            },
        },
        {
            "id": 11,
            "type": "image",
            "props": {
                "image_mode": "RGB",
                "source": "upload",
                "tool": "editor",
                "streaming": False,
                "mirror_webcam": True,
                "show_label": True,
                "name": "image",
                "visible": True,
                "style": {},
            },
            "serializer": "ImgSerializable",
            "info": {
                "input": ["str", "filepath or URL"],
                "output": ["str", "filepath or URL"],
            },
        },
        {
            "id": 12,
            "type": "json",
            "props": {"show_label": True, "name": "json", "visible": True, "style": {}},
            "serializer": "JSONSerializable",
            "info": {
                "input": ["str", "filepath to json file"],
                "output": ["str", "filepath to json file"],
            },
        },
        {
            "id": 13,
            "type": "button",
            "props": {
                "value": "Run",
                "variant": "secondary",
                "interactive": True,
                "name": "button",
                "visible": True,
                "style": {},
            },
            "serializer": "Serializable",
            "info": {"input": ["str", "value"], "output": ["str", "value"]},
        },
        {
            "id": 14,
            "type": "textbox",
            "props": {
                "lines": 1,
                "max_lines": 20,
                "value": "",
                "type": "text",
                "show_label": True,
                "name": "textbox",
                "visible": True,
                "style": {},
            },
            "serializer": "Serializable",
            "info": {"input": ["str", "value"], "output": ["str", "value"]},
        },
        {
            "id": 15,
            "type": "form",
            "props": {"type": "form", "visible": True, "style": {}},
        },
        {
            "id": 16,
            "type": "form",
            "props": {"type": "form", "visible": True, "style": {}},
        },
    ],
    "css": None,
    "title": "Gradio",
    "is_space": False,
    "enable_queue": None,
    "show_error": True,
    "show_api": True,
    "is_colab": False,
    "stylesheets": [
        "https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@400;600&display=swap",
        "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&display=swap",
    ],
    "root": "",
    "theme": "default",
    "layout": {
        "id": 0,
        "children": [
            {"id": 1},
            {"id": 15, "children": [{"id": 2}]},
            {
                "id": 3,
                "children": [
                    {
                        "id": 4,
                        "children": [
                            {"id": 5, "children": [{"id": 6}, {"id": 7}]},
                            {"id": 8},
                        ],
                    },
                    {
                        "id": 9,
                        "children": [
                            {"id": 10, "children": [{"id": 11}, {"id": 12}]},
                            {"id": 13},
                        ],
                    },
                ],
            },
            {"id": 16, "children": [{"id": 14}]},
        ],
    },
    "dependencies": [
        {
            "targets": [8],
            "trigger": "click",
            "inputs": [2, 6],
            "outputs": [7],
            "backend_fn": True,
            "js": None,
            "queue": None,
            "api_name": None,
            "scroll_to_output": False,
            "show_progress": True,
            "every": None,
            "batch": False,
            "max_batch_size": 4,
            "cancels": [],
            "types": {"continuous": False, "generator": False},
            "collects_event_data": False,
            "trigger_after": None,
            "trigger_only_on_success": False,
        },
        {
            "targets": [13],
            "trigger": "click",
            "inputs": [2, 11],
            "outputs": [12],
            "backend_fn": True,
            "js": None,
            "queue": None,
            "api_name": None,
            "scroll_to_output": False,
            "show_progress": True,
            "every": None,
            "batch": False,
            "max_batch_size": 4,
            "cancels": [],
            "types": {"continuous": False, "generator": False},
            "collects_event_data": False,
            "trigger_after": None,
            "trigger_only_on_success": False,
        },
        {
            "targets": [],
            "trigger": "load",
            "inputs": [],
            "outputs": [14],
            "backend_fn": True,
            "js": None,
            "queue": None,
            "api_name": None,
            "scroll_to_output": False,
            "show_progress": True,
            "every": None,
            "batch": False,
            "max_batch_size": 4,
            "cancels": [],
            "types": {"continuous": False, "generator": False},
            "collects_event_data": False,
            "trigger_after": None,
            "trigger_only_on_success": False,
        },
    ],
}


XRAY_CONFIG_DIFF_IDS = {
    "version": "3.23.1b3",
    "mode": "blocks",
    "dev_mode": True,
    "analytics_enabled": False,
    "components": [
        {
            "id": 1,
            "type": "markdown",
            "props": {
                "value": "<h1>Detect Disease From Scan</h1>\n<p>With this model you can lorem ipsum</p>\n<ul>\n<li>ipsum 1</li>\n<li>ipsum 2</li>\n</ul>\n",
                "name": "markdown",
                "visible": True,
                "style": {},
            },
            "serializer": "Serializable",
            "info": {"input": ["str", "value"], "output": ["str", "value"]},
        },
        {
            "id": 2,
            "type": "checkboxgroup",
            "props": {
                "choices": ["Covid", "Malaria", "Lung Cancer"],
                "value": [],
                "label": "Disease to Scan For",
                "show_label": True,
                "name": "checkboxgroup",
                "visible": True,
                "style": {},
            },
            "serializer": "Serializable",
            "info": {
                "input": ["List[str]", "values"],
                "output": ["List[str]", "values"],
            },
        },
        {"id": 3, "type": "tabs", "props": {"visible": True, "style": {}}},
        {
            "id": 4,
            "type": "tabitem",
            "props": {"label": "X-ray", "visible": True, "style": {}},
        },
        {
            "id": 5,
            "type": "row",
            "props": {
                "type": "row",
                "variant": "default",
                "visible": True,
                "style": {},
            },
        },
        {
            "id": 6,
            "type": "image",
            "props": {
                "image_mode": "RGB",
                "source": "upload",
                "tool": "editor",
                "streaming": False,
                "mirror_webcam": True,
                "show_label": True,
                "name": "image",
                "visible": True,
                "style": {},
            },
            "serializer": "ImgSerializable",
            "info": {
                "input": ["str", "filepath or URL"],
                "output": ["str", "filepath or URL"],
            },
        },
        {
            "id": 7,
            "type": "json",
            "props": {"show_label": True, "name": "json", "visible": True, "style": {}},
            "serializer": "JSONSerializable",
            "info": {
                "input": ["str", "filepath to json file"],
                "output": ["str", "filepath to json file"],
            },
        },
        {
            "id": 8,
            "type": "button",
            "props": {
                "value": "Run",
                "variant": "secondary",
                "interactive": True,
                "name": "button",
                "visible": True,
                "style": {},
            },
            "serializer": "Serializable",
            "info": {"input": ["str", "value"], "output": ["str", "value"]},
        },
        {
            "id": 9,
            "type": "tabitem",
            "props": {"label": "CT Scan", "visible": True, "style": {}},
        },
        {
            "id": 10,
            "type": "row",
            "props": {
                "type": "row",
                "variant": "default",
                "visible": True,
                "style": {},
            },
        },
        {
            "id": 11,
            "type": "image",
            "props": {
                "image_mode": "RGB",
                "source": "upload",
                "tool": "editor",
                "streaming": False,
                "mirror_webcam": True,
                "show_label": True,
                "name": "image",
                "visible": True,
                "style": {},
            },
            "serializer": "ImgSerializable",
            "info": {
                "input": ["str", "filepath or URL"],
                "output": ["str", "filepath or URL"],
            },
        },
        {
            "id": 1212,
            "type": "json",
            "props": {"show_label": True, "name": "json", "visible": True, "style": {}},
            "serializer": "JSONSerializable",
            "info": {
                "input": ["str", "filepath to json file"],
                "output": ["str", "filepath to json file"],
            },
        },
        {
            "id": 13,
            "type": "button",
            "props": {
                "value": "Run",
                "variant": "secondary",
                "interactive": True,
                "name": "button",
                "visible": True,
                "style": {},
            },
            "serializer": "Serializable",
            "info": {"input": ["str", "value"], "output": ["str", "value"]},
        },
        {
            "id": 14,
            "type": "textbox",
            "props": {
                "lines": 1,
                "max_lines": 20,
                "value": "",
                "type": "text",
                "show_label": True,
                "name": "textbox",
                "visible": True,
                "style": {},
            },
            "serializer": "Serializable",
            "info": {"input": ["str", "value"], "output": ["str", "value"]},
        },
        {
            "id": 15,
            "type": "form",
            "props": {"type": "form", "visible": True, "style": {}},
        },
        {
            "id": 16,
            "type": "form",
            "props": {"type": "form", "visible": True, "style": {}},
        },
    ],
    "css": None,
    "title": "Gradio",
    "is_space": False,
    "enable_queue": None,
    "show_error": True,
    "show_api": True,
    "is_colab": False,
    "stylesheets": [
        "https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@400;600&display=swap",
        "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&display=swap",
    ],
    "root": "",
    "theme": "default",
    "layout": {
        "id": 0,
        "children": [
            {"id": 1},
            {"id": 15, "children": [{"id": 2}]},
            {
                "id": 3,
                "children": [
                    {
                        "id": 4,
                        "children": [
                            {"id": 5, "children": [{"id": 6}, {"id": 7}]},
                            {"id": 8},
                        ],
                    },
                    {
                        "id": 9,
                        "children": [
                            {"id": 10, "children": [{"id": 11}, {"id": 1212}]},
                            {"id": 13},
                        ],
                    },
                ],
            },
            {"id": 16, "children": [{"id": 14}]},
        ],
    },
    "dependencies": [
        {
            "targets": [8],
            "trigger": "click",
            "inputs": [2, 6],
            "outputs": [7],
            "backend_fn": True,
            "js": None,
            "queue": None,
            "api_name": None,
            "scroll_to_output": False,
            "show_progress": True,
            "every": None,
            "batch": False,
            "max_batch_size": 4,
            "cancels": [],
            "types": {"continuous": False, "generator": False},
            "collects_event_data": False,
            "trigger_after": None,
            "trigger_only_on_success": False,
        },
        {
            "targets": [13],
            "trigger": "click",
            "inputs": [2, 11],
            "outputs": [1212],
            "backend_fn": True,
            "js": None,
            "queue": None,
            "api_name": None,
            "scroll_to_output": False,
            "show_progress": True,
            "every": None,
            "batch": False,
            "max_batch_size": 4,
            "cancels": [],
            "types": {"continuous": False, "generator": False},
            "collects_event_data": False,
            "trigger_after": None,
            "trigger_only_on_success": False,
        },
        {
            "targets": [],
            "trigger": "load",
            "inputs": [],
            "outputs": [14],
            "backend_fn": True,
            "js": None,
            "queue": None,
            "api_name": None,
            "scroll_to_output": False,
            "show_progress": True,
            "every": None,
            "batch": False,
            "max_batch_size": 4,
            "cancels": [],
            "types": {"continuous": False, "generator": False},
            "collects_event_data": False,
            "trigger_after": None,
            "trigger_only_on_success": False,
        },
    ],
}


XRAY_CONFIG_WITH_MISTAKE = {
    "mode": "blocks",
    "dev_mode": True,
    "analytics_enabled": False,
    "theme": "default",
    "components": [
        {
            "id": 1,
            "type": "markdown",
            "props": {
                "value": "<h1>Detect Disease From Scan</h1>\n<p>With this model you can lorem ipsum</p>\n<ul>\n<li>ipsum 1</li>\n<li>ipsum 2</li>\n</ul>\n",
                "name": "markdown",
                "style": {},
            },
        },
        {
            "id": 2,
            "type": "checkboxgroup",
            "props": {
                "choices": ["Covid", "Malaria", "Lung Cancer"],
                "value": [],
                "name": "checkboxgroup",
                "show_label": True,
                "label": "Disease to Scan For",
                "style": {},
            },
        },
        {
            "id": 3,
            "type": "tabs",
            "props": {
                "style": {},
                "value": True,
            },
        },
        {
            "id": 4,
            "type": "tabitem",
            "props": {
                "label": "X-ray",
                "style": {},
                "value": True,
            },
        },
        {
            "id": 5,
            "type": "row",
            "props": {"type": "row", "variant": "default", "style": {}, "value": True},
        },
        {
            "id": 6,
            "type": "image",
            "props": {
                "image_mode": "RGB",
                "source": "upload",
                "streaming": False,
                "mirror_webcam": True,
                "tool": "editor",
                "name": "image",
                "style": {},
            },
        },
        {
            "id": 7,
            "type": "json",
            "props": {
                "name": "json",
                "style": {},
            },
        },
        {
            "id": 8,
            "type": "button",
            "props": {
                "value": "Run",
                "name": "button",
                "interactive": True,
                "css": {"background-color": "red", "--hover-color": "orange"},
                "variant": "secondary",
            },
        },
        {
            "id": 9,
            "type": "tabitem",
            "props": {
                "show_label": True,
                "label": "CT Scan",
                "style": {},
                "value": True,
            },
        },
        {
            "id": 10,
            "type": "row",
            "props": {"type": "row", "variant": "default", "style": {}, "value": True},
        },
        {
            "id": 11,
            "type": "image",
            "props": {
                "image_mode": "RGB",
                "source": "upload",
                "tool": "editor",
                "streaming": False,
                "mirror_webcam": True,
                "name": "image",
                "style": {},
            },
        },
        {
            "id": 12,
            "type": "json",
            "props": {
                "name": "json",
                "style": {},
            },
        },
        {
            "id": 13,
            "type": "button",
            "props": {
                "value": "Run",
                "interactive": True,
                "name": "button",
                "style": {},
                "variant": "secondary",
            },
        },
        {
            "id": 14,
            "type": "textbox",
            "props": {
                "lines": 1,
                "value": "",
                "name": "textbox",
                "type": "text",
                "style": {},
            },
        },
    ],
    "layout": {
        "id": 0,
        "children": [
            {"id": 1},
            {"id": 2},
            {
                "id": 3,
                "children": [
                    {
                        "id": 4,
                        "children": [
                            {"id": 5, "children": [{"id": 6}, {"id": 7}]},
                            {"id": 8},
                        ],
                    },
                    {
                        "id": 9,
                        "children": [
                            {"id": 10, "children": [{"id": 12}, {"id": 11}]},
                            {"id": 13},
                        ],
                    },
                ],
            },
            {"id": 14},
        ],
    },
    "dependencies": [
        {
            "targets": [8],
            "trigger": "click",
            "inputs": [2, 6],
            "outputs": [7],
            "api_name": None,
            "scroll_to_output": False,
            "show_progress": True,
            "cancels": [],
            "trigger_after": None,
            "trigger_only_on_success": False,
        },
        {
            "targets": [13],
            "trigger": "click",
            "inputs": [2, 11],
            "outputs": [12],
            "api_name": None,
            "scroll_to_output": False,
            "show_progress": True,
            "cancels": [],
            "trigger_after": None,
            "trigger_only_on_success": False,
        },
    ],
}
