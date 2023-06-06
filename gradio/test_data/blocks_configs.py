XRAY_CONFIG = {
    "version": "3.32.0\n",
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
            },
            "serializer": "StringSerializable",
            "api_info": {"info": {"type": "string"}, "serialized_info": False},
            "example_inputs": {"raw": "Howdy!", "serialized": "Howdy!"},
        },
        {
            "id": 2,
            "type": "checkboxgroup",
            "props": {
                "choices": ["Covid", "Malaria", "Lung Cancer"],
                "value": [],
                "label": "Disease to Scan For",
                "show_label": True,
                "container": True,
                "min_width": 160,
                "name": "checkboxgroup",
                "visible": True,
            },
            "serializer": "ListStringSerializable",
            "api_info": {
                "info": {"type": "array", "items": {"type": "string"}},
                "serialized_info": False,
            },
            "example_inputs": {"raw": "Covid", "serialized": "Covid"},
        },
        {"id": 3, "type": "tabs", "props": {"visible": True}},
        {"id": 4, "type": "tabitem", "props": {"label": "X-ray", "visible": True}},
        {
            "id": 5,
            "type": "row",
            "props": {
                "type": "row",
                "variant": "default",
                "equal_height": True,
                "visible": True,
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
                "selectable": False,
                "show_label": True,
                "container": True,
                "min_width": 160,
                "name": "image",
                "visible": True,
            },
            "serializer": "ImgSerializable",
            "api_info": {
                "info": {
                    "type": "string",
                    "description": "base64 representation of an image",
                },
                "serialized_info": True,
            },
            "example_inputs": {
                "raw": "data:image/png;base64,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",
                "serialized": "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",
            },
        },
        {
            "id": 7,
            "type": "json",
            "props": {
                "show_label": True,
                "container": True,
                "min_width": 160,
                "name": "json",
                "visible": True,
            },
            "serializer": "JSONSerializable",
            "api_info": {
                "info": {"type": {}, "description": "any valid json"},
                "serialized_info": True,
            },
            "example_inputs": {"raw": {"a": 1, "b": 2}, "serialized": None},
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
            },
            "serializer": "StringSerializable",
            "api_info": {"info": {"type": "string"}, "serialized_info": False},
            "example_inputs": {"raw": "Howdy!", "serialized": "Howdy!"},
        },
        {"id": 9, "type": "tabitem", "props": {"label": "CT Scan", "visible": True}},
        {
            "id": 10,
            "type": "row",
            "props": {
                "type": "row",
                "variant": "default",
                "equal_height": True,
                "visible": True,
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
                "selectable": False,
                "show_label": True,
                "container": True,
                "min_width": 160,
                "name": "image",
                "visible": True,
            },
            "serializer": "ImgSerializable",
            "api_info": {
                "info": {
                    "type": "string",
                    "description": "base64 representation of an image",
                },
                "serialized_info": True,
            },
            "example_inputs": {
                "raw": "data:image/png;base64,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",
                "serialized": "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",
            },
        },
        {
            "id": 12,
            "type": "json",
            "props": {
                "show_label": True,
                "container": True,
                "min_width": 160,
                "name": "json",
                "visible": True,
            },
            "serializer": "JSONSerializable",
            "api_info": {
                "info": {"type": {}, "description": "any valid json"},
                "serialized_info": True,
            },
            "example_inputs": {"raw": {"a": 1, "b": 2}, "serialized": None},
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
            },
            "serializer": "StringSerializable",
            "api_info": {"info": {"type": "string"}, "serialized_info": False},
            "example_inputs": {"raw": "Howdy!", "serialized": "Howdy!"},
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
                "container": True,
                "min_width": 160,
                "name": "textbox",
                "visible": True,
            },
            "serializer": "StringSerializable",
            "api_info": {"info": {"type": "string"}, "serialized_info": False},
            "example_inputs": {"raw": "Howdy!", "serialized": "Howdy!"},
        },
        {
            "id": 15,
            "type": "form",
            "props": {"type": "form", "scale": 0, "min_width": 0, "visible": True},
        },
        {
            "id": 16,
            "type": "form",
            "props": {"type": "form", "scale": 0, "min_width": 0, "visible": True},
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
            "show_progress": "full",
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
            "show_progress": "full",
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
            "show_progress": "full",
        },
    ],
}

XRAY_CONFIG_DIFF_IDS = {
    "version": "3.32.0\n",
    "mode": "blocks",
    "dev_mode": True,
    "analytics_enabled": False,
    "components": [
        {
            "id": 6,
            "type": "markdown",
            "props": {
                "value": "<h1>Detect Disease From Scan</h1>\n<p>With this model you can lorem ipsum</p>\n<ul>\n<li>ipsum 1</li>\n<li>ipsum 2</li>\n</ul>\n",
                "name": "markdown",
                "visible": True,
            },
            "serializer": "StringSerializable",
            "api_info": {"info": {"type": "string"}, "serialized_info": False},
            "example_inputs": {"raw": "Howdy!", "serialized": "Howdy!"},
        },
        {
            "id": 7,
            "type": "checkboxgroup",
            "props": {
                "choices": ["Covid", "Malaria", "Lung Cancer"],
                "value": [],
                "label": "Disease to Scan For",
                "show_label": True,
                "container": True,
                "min_width": 160,
                "name": "checkboxgroup",
                "visible": True,
            },
            "serializer": "ListStringSerializable",
            "api_info": {
                "info": {"type": "array", "items": {"type": "string"}},
                "serialized_info": False,
            },
            "example_inputs": {"raw": "Covid", "serialized": "Covid"},
        },
        {"id": 8, "type": "tabs", "props": {"visible": True}},
        {"id": 9, "type": "tabitem", "props": {"label": "X-ray", "visible": True}},
        {
            "id": 10,
            "type": "row",
            "props": {
                "type": "row",
                "variant": "default",
                "equal_height": True,
                "visible": True,
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
                "selectable": False,
                "show_label": True,
                "container": True,
                "min_width": 160,
                "name": "image",
                "visible": True,
            },
            "serializer": "ImgSerializable",
            "api_info": {
                "info": {
                    "type": "string",
                    "description": "base64 representation of an image",
                },
                "serialized_info": True,
            },
            "example_inputs": {
                "raw": "data:image/png;base64,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",
                "serialized": "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",
            },
        },
        {
            "id": 12,
            "type": "json",
            "props": {
                "show_label": True,
                "container": True,
                "min_width": 160,
                "name": "json",
                "visible": True,
            },
            "serializer": "JSONSerializable",
            "api_info": {
                "info": {"type": {}, "description": "any valid json"},
                "serialized_info": True,
            },
            "example_inputs": {"raw": {"a": 1, "b": 2}, "serialized": None},
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
            },
            "serializer": "StringSerializable",
            "api_info": {"info": {"type": "string"}, "serialized_info": False},
            "example_inputs": {"raw": "Howdy!", "serialized": "Howdy!"},
        },
        {"id": 14, "type": "tabitem", "props": {"label": "CT Scan", "visible": True}},
        {
            "id": 15,
            "type": "row",
            "props": {
                "type": "row",
                "variant": "default",
                "equal_height": True,
                "visible": True,
            },
        },
        {
            "id": 16,
            "type": "image",
            "props": {
                "image_mode": "RGB",
                "source": "upload",
                "tool": "editor",
                "streaming": False,
                "mirror_webcam": True,
                "selectable": False,
                "show_label": True,
                "container": True,
                "min_width": 160,
                "name": "image",
                "visible": True,
            },
            "serializer": "ImgSerializable",
            "api_info": {
                "info": {
                    "type": "string",
                    "description": "base64 representation of an image",
                },
                "serialized_info": True,
            },
            "example_inputs": {
                "raw": "data:image/png;base64,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",
                "serialized": "https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png",
            },
        },
        {
            "id": 17,
            "type": "json",
            "props": {
                "show_label": True,
                "container": True,
                "min_width": 160,
                "name": "json",
                "visible": True,
            },
            "serializer": "JSONSerializable",
            "api_info": {
                "info": {"type": {}, "description": "any valid json"},
                "serialized_info": True,
            },
            "example_inputs": {"raw": {"a": 1, "b": 2}, "serialized": None},
        },
        {
            "id": 18,
            "type": "button",
            "props": {
                "value": "Run",
                "variant": "secondary",
                "interactive": True,
                "name": "button",
                "visible": True,
            },
            "serializer": "StringSerializable",
            "api_info": {"info": {"type": "string"}, "serialized_info": False},
            "example_inputs": {"raw": "Howdy!", "serialized": "Howdy!"},
        },
        {
            "id": 19,
            "type": "textbox",
            "props": {
                "lines": 1,
                "max_lines": 20,
                "value": "",
                "type": "text",
                "show_label": True,
                "container": True,
                "min_width": 160,
                "name": "textbox",
                "visible": True,
            },
            "serializer": "StringSerializable",
            "api_info": {"info": {"type": "string"}, "serialized_info": False},
            "example_inputs": {"raw": "Howdy!", "serialized": "Howdy!"},
        },
        {
            "id": 20,
            "type": "form",
            "props": {"type": "form", "scale": 0, "min_width": 0, "visible": True},
        },
        {
            "id": 21,
            "type": "form",
            "props": {"type": "form", "scale": 0, "min_width": 0, "visible": True},
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
    "theme": "default",
    "layout": {
        "id": 0,
        "children": [
            {"id": 6},
            {"id": 20, "children": [{"id": 7}]},
            {
                "id": 8,
                "children": [
                    {
                        "id": 9,
                        "children": [
                            {"id": 10, "children": [{"id": 11}, {"id": 12}]},
                            {"id": 12},
                        ],
                    },
                    {
                        "id": 14,
                        "children": [
                            {"id": 15, "children": [{"id": 16}, {"id": 17}]},
                            {"id": 18},
                        ],
                    },
                ],
            },
            {"id": 21, "children": [{"id": 19}]},
        ],
    },
    "dependencies": [
        {
            "targets": [13],
            "trigger": "click",
            "inputs": [7, 11],
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
            "show_progress": "full",
        },
        {
            "targets": [18],
            "trigger": "click",
            "inputs": [17, 16],
            "outputs": [17],
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
            "show_progress": "full",
        },
        {
            "targets": [],
            "trigger": "load",
            "inputs": [],
            "outputs": [19],
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
            "show_progress": "full",
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
                "container": True,
                "min_width": 160,
            },
        },
        {
            "id": 3,
            "type": "tabs",
            "props": {
                "value": True,
            },
        },
        {
            "id": 4,
            "type": "tabitem",
            "props": {
                "label": "X-ray",
                "value": True,
            },
        },
        {
            "id": 5,
            "type": "row",
            "props": {
                "type": "row",
                "variant": "default",
                "equal_height": True,
                "value": True,
            },
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
                "selectable": False,
            },
        },
        {
            "id": 7,
            "type": "json",
            "props": {
                "name": "json",
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
                "value": True,
            },
        },
        {
            "id": 10,
            "type": "row",
            "props": {
                "type": "row",
                "variant": "default",
                "equal_height": True,
                "value": True,
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
                "name": "image",
                "selectable": False,
            },
        },
        {
            "id": 12,
            "type": "json",
            "props": {
                "name": "json",
            },
        },
        {
            "id": 13,
            "type": "button",
            "props": {
                "value": "Run",
                "interactive": True,
                "name": "button",
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
            "show_progress": "full",
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
            "show_progress": "full",
        },
    ],
}
