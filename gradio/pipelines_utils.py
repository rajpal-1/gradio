"""
Defines internal helper methods for handling transformers and diffusers pipelines.
These are used by load_from_pipeline method in pipelines.py.
"""

from typing import Any, Dict, Optional

from PIL import Image

from gradio import components


def handle_transformers_pipeline(pipeline: Any) -> Optional[Dict[str, Any]]:
    try:
        import transformers
    except ImportError as ie:
        raise ImportError(
            "transformers not installed. Please try `pip install transformers`"
        ) from ie

    def is_transformers_pipeline_type(pipeline, class_name: str):
        cls = getattr(transformers, class_name, None)
        return cls and isinstance(pipeline, cls)

    # Handle the different pipelines. The has_attr() checks to make sure the pipeline exists in the
    # version of the transformers library that the user has installed.
    if is_transformers_pipeline_type(pipeline, "AudioClassificationPipeline"):
        return {
            "inputs": components.Audio(
                sources=["microphone"],
                type="filepath",
                label="Input",
                render=False,
            ),
            "outputs": components.Label(label="Class", render=False),
            "preprocess": lambda i: {"inputs": i},
            "postprocess": lambda r: {i["label"].split(", ")[0]: i["score"] for i in r},
        }
    if is_transformers_pipeline_type(pipeline, "AutomaticSpeechRecognitionPipeline"):
        return {
            "inputs": components.Audio(
                sources=["microphone"], type="filepath", label="Input", render=False
            ),
            "outputs": components.Textbox(label="Output", render=False),
            "preprocess": lambda i: {"inputs": i},
            "postprocess": lambda r: r["text"],
        }
    if is_transformers_pipeline_type(pipeline, "FeatureExtractionPipeline"):
        return {
            "inputs": components.Textbox(label="Input", render=False),
            "outputs": components.Dataframe(label="Output", render=False),
            "preprocess": lambda x: {"inputs": x},
            "postprocess": lambda r: r[0],
        }
    if is_transformers_pipeline_type(pipeline, "FillMaskPipeline"):
        return {
            "inputs": components.Textbox(label="Input", render=False),
            "outputs": components.Label(label="Classification", render=False),
            "preprocess": lambda x: {"inputs": x},
            "postprocess": lambda r: {i["token_str"]: i["score"] for i in r},
        }
    if is_transformers_pipeline_type(pipeline, "ImageClassificationPipeline"):
        return {
            "inputs": components.Image(
                type="filepath", label="Input Image", render=False
            ),
            "outputs": components.Label(label="Classification", render=False),
            "preprocess": lambda i: {"images": i},
            "postprocess": lambda r: {i["label"].split(", ")[0]: i["score"] for i in r},
        }
    if is_transformers_pipeline_type(pipeline, "QuestionAnsweringPipeline"):
        return {
            "inputs": [
                components.Textbox(lines=7, label="Context", render=False),
                components.Textbox(label="Question", render=False),
            ],
            "outputs": [
                components.Textbox(label="Answer", render=False),
                components.Label(label="Score", render=False),
            ],
            "preprocess": lambda c, q: {"context": c, "question": q},
            "postprocess": lambda r: (r["answer"], r["score"]),
        }
    if is_transformers_pipeline_type(pipeline, "SummarizationPipeline"):
        return {
            "inputs": components.Textbox(lines=7, label="Input", render=False),
            "outputs": components.Textbox(label="Summary", render=False),
            "preprocess": lambda x: {"inputs": x},
            "postprocess": lambda r: r[0]["summary_text"],
        }
    if is_transformers_pipeline_type(pipeline, "TextClassificationPipeline"):
        return {
            "inputs": components.Textbox(label="Input", render=False),
            "outputs": components.Label(label="Classification", render=False),
            "preprocess": lambda x: [x],
            "postprocess": lambda r: {i["label"].split(", ")[0]: i["score"] for i in r},
        }
    if is_transformers_pipeline_type(pipeline, "TextGenerationPipeline"):
        return {
            "inputs": components.Textbox(label="Input", render=False),
            "outputs": components.Textbox(label="Output", render=False),
            "preprocess": lambda x: {"text_inputs": x},
            "postprocess": lambda r: r[0]["generated_text"],
        }
    if is_transformers_pipeline_type(pipeline, "TranslationPipeline"):
        return {
            "inputs": components.Textbox(label="Input", render=False),
            "outputs": components.Textbox(label="Translation", render=False),
            "preprocess": lambda x: [x],
            "postprocess": lambda r: r[0]["translation_text"],
        }
    if is_transformers_pipeline_type(pipeline, "Text2TextGenerationPipeline"):
        return {
            "inputs": components.Textbox(label="Input", render=False),
            "outputs": components.Textbox(label="Generated Text", render=False),
            "preprocess": lambda x: [x],
            "postprocess": lambda r: r[0]["generated_text"],
        }
    if is_transformers_pipeline_type(pipeline, "ZeroShotClassificationPipeline"):
        return {
            "inputs": [
                components.Textbox(label="Input", render=False),
                components.Textbox(
                    label="Possible class names (comma-separated)", render=False
                ),
                components.Checkbox(label="Allow multiple true classes", render=False),
            ],
            "outputs": components.Label(label="Classification", render=False),
            "preprocess": lambda i, c, m: {
                "sequences": i,
                "candidate_labels": c,
                "multi_label": m,
            },
            "postprocess": lambda r: {
                r["labels"][i]: r["scores"][i] for i in range(len(r["labels"]))
            },
        }
    if is_transformers_pipeline_type(pipeline, "DocumentQuestionAnsweringPipeline"):
        return {
            "inputs": [
                components.Image(type="filepath", label="Input Document", render=False),
                components.Textbox(label="Question", render=False),
            ],
            "outputs": components.Label(label="Label", render=False),
            "preprocess": lambda img, q: {"image": img, "question": q},
            "postprocess": lambda r: {i["answer"]: i["score"] for i in r},
        }
    if is_transformers_pipeline_type(pipeline, "VisualQuestionAnsweringPipeline"):
        return {
            "inputs": [
                components.Image(type="filepath", label="Input Image", render=False),
                components.Textbox(label="Question", render=False),
            ],
            "outputs": components.Label(label="Score", render=False),
            "preprocess": lambda img, q: {"image": img, "question": q},
            "postprocess": lambda r: {i["answer"]: i["score"] for i in r},
        }
    if is_transformers_pipeline_type(pipeline, "ImageToTextPipeline"):
        return {
            "inputs": components.Image(
                type="filepath", label="Input Image", render=False
            ),
            "outputs": components.Textbox(label="Text", render=False),
            "preprocess": lambda i: {"images": i},
            "postprocess": lambda r: r[0]["generated_text"],
        }
    if is_transformers_pipeline_type(pipeline, "ObjectDetectionPipeline"):
        return {
            "inputs": components.Image(
                type="filepath", label="Input Image", render=False
            ),
            "outputs": components.AnnotatedImage(
                label="Objects Detected", render=False
            ),
            "preprocess": lambda i: {"inputs": i},
            "postprocess": lambda r, img: (
                img,
                [
                    (
                        (
                            i["box"]["xmin"],
                            i["box"]["ymin"],
                            i["box"]["xmax"],
                            i["box"]["ymax"],
                        ),
                        i["label"],
                    )
                    for i in r
                ],
            ),
        }
    raise ValueError(f"Unsupported transformers pipeline type: {type(pipeline)}")


def handle_diffusers_pipeline(pipeline: Any) -> Optional[Dict[str, Any]]:
    try:
        import diffusers
    except ImportError as ie:
        raise ImportError(
            "diffusers not installed. Please try `pip install diffusers`"
        ) from ie

    def is_diffusers_pipeline_type(pipeline, class_name: str):
        cls = getattr(diffusers, class_name, None)
        return cls and isinstance(pipeline, cls)

    if is_diffusers_pipeline_type(pipeline, "StableDiffusionPipeline"):
        return {
            "inputs": [
                components.Textbox(label="Prompt", render=False),
                components.Textbox(label="Negative prompt", render=False),
                components.Slider(
                    label="Number of inference steps",
                    minimum=1,
                    maximum=500,
                    value=50,
                    step=1,
                ),
                components.Slider(
                    label="Guidance scale",
                    minimum=1,
                    maximum=20,
                    value=7.5,
                    step=0.5,
                ),
            ],
            "outputs": components.Image(
                label="Generated Image", render=False, type="pil"
            ),
            "preprocess": lambda prompt, n_prompt, num_inf_steps, g_scale: {
                "prompt": prompt,
                "negative_prompt": n_prompt,
                "num_inference_steps": num_inf_steps,
                "guidance_scale": g_scale,
            },
            "postprocess": lambda r: r["images"][0],
        }
    if is_diffusers_pipeline_type(pipeline, "StableDiffusionImg2ImgPipeline"):
        return {
            "inputs": [
                components.Textbox(label="Prompt", render=False),
                components.Textbox(label="Negative prompt", render=False),
                components.Image(type="filepath", label="Image", render=False),
                components.Slider(
                    label="Strength", minimum=0, maximum=1, value=0.8, step=0.1
                ),
                components.Slider(
                    label="Number of inference steps",
                    minimum=1,
                    maximum=500,
                    value=50,
                    step=1,
                ),
                components.Slider(
                    label="Guidance scale",
                    minimum=1,
                    maximum=20,
                    value=7.5,
                    step=0.5,
                ),
            ],
            "outputs": components.Image(
                label="Generated Image", render=False, type="pil"
            ),
            "preprocess": lambda prompt,
            n_prompt,
            image,
            strength,
            num_inf_steps,
            g_scale: {
                "prompt": prompt,
                "image": Image.open(image).resize((768, 768)),
                "negative_prompt": n_prompt,
                "num_inference_steps": num_inf_steps,
                "guidance_scale": g_scale,
                "strength": strength,
            },
            "postprocess": lambda r: r["images"][0],
        }
    if is_diffusers_pipeline_type(pipeline, "StableDiffusionInpaintPipeline"):
        return {
            "inputs": [
                components.Textbox(label="Prompt", render=False),
                components.Textbox(label="Negative prompt", render=False),
                components.Image(type="filepath", label="Image", render=False),
                components.Image(type="filepath", label="Mask Image", render=False),
                components.Slider(
                    label="Strength", minimum=0, maximum=1, value=0.8, step=0.1
                ),
                components.Slider(
                    label="Number of inference steps",
                    minimum=1,
                    maximum=500,
                    value=50,
                    step=1,
                ),
                components.Slider(
                    label="Guidance scale",
                    minimum=1,
                    maximum=20,
                    value=7.5,
                    step=0.5,
                ),
            ],
            "outputs": components.Image(
                label="Generated Image", render=False, type="pil"
            ),
            "preprocess": lambda prompt,
            n_prompt,
            image,
            mask_image,
            strength,
            num_inf_steps,
            g_scale: {
                "prompt": prompt,
                "image": Image.open(image).resize((768, 768)),
                "mask_image": Image.open(mask_image).resize((768, 768)),
                "negative_prompt": n_prompt,
                "num_inference_steps": num_inf_steps,
                "guidance_scale": g_scale,
                "strength": strength,
            },
            "postprocess": lambda r: r["images"][0],
        }
    if is_diffusers_pipeline_type(pipeline, "StableDiffusionDepth2ImgPipeline"):
        return {
            "inputs": [
                components.Textbox(label="Prompt", render=False),
                components.Textbox(label="Negative prompt", render=False),
                components.Image(type="filepath", label="Image", render=False),
                components.Slider(
                    label="Strength", minimum=0, maximum=1, value=0.8, step=0.1
                ),
                components.Slider(
                    label="Number of inference steps",
                    minimum=1,
                    maximum=500,
                    value=50,
                    step=1,
                ),
                components.Slider(
                    label="Guidance scale",
                    minimum=1,
                    maximum=20,
                    value=7.5,
                    step=0.5,
                ),
            ],
            "outputs": components.Image(
                label="Generated Image", render=False, type="pil"
            ),
            "preprocess": lambda prompt,
            n_prompt,
            image,
            strength,
            num_inf_steps,
            g_scale: {
                "prompt": prompt,
                "image": Image.open(image).resize((768, 768)),
                "negative_prompt": n_prompt,
                "num_inference_steps": num_inf_steps,
                "guidance_scale": g_scale,
                "strength": strength,
            },
            "postprocess": lambda r: r["images"][0],
        }
    if is_diffusers_pipeline_type(pipeline, "StableDiffusionImageVariationPipeline"):
        return {
            "inputs": [
                components.Image(type="filepath", label="Image", render=False),
                components.Slider(
                    label="Number of inference steps",
                    minimum=1,
                    maximum=500,
                    value=50,
                    step=1,
                ),
                components.Slider(
                    label="Guidance scale",
                    minimum=1,
                    maximum=20,
                    value=7.5,
                    step=0.5,
                ),
            ],
            "outputs": components.Image(
                label="Generated Image", render=False, type="pil"
            ),
            "preprocess": lambda image, num_inf_steps, g_scale: {
                "image": Image.open(image).resize((768, 768)),
                "num_inference_steps": num_inf_steps,
                "guidance_scale": g_scale,
            },
            "postprocess": lambda r: r["images"][0],
        }
    if is_diffusers_pipeline_type(pipeline, "StableDiffusionInstructPix2PixPipeline"):
        return {
            "inputs": [
                components.Textbox(label="Prompt", render=False),
                components.Textbox(label="Negative prompt", render=False),
                components.Image(type="filepath", label="Image", render=False),
                components.Slider(
                    label="Number of inference steps",
                    minimum=1,
                    maximum=500,
                    value=50,
                    step=1,
                ),
                components.Slider(
                    label="Guidance scale",
                    minimum=1,
                    maximum=20,
                    value=7.5,
                    step=0.5,
                ),
                components.Slider(
                    label="Image Guidance scale",
                    minimum=1,
                    maximum=5,
                    value=1.5,
                    step=0.5,
                ),
            ],
            "outputs": components.Image(
                label="Generated Image", render=False, type="pil"
            ),
            "preprocess": lambda prompt,
            n_prompt,
            image,
            num_inf_steps,
            g_scale,
            img_g_scale: {
                "prompt": prompt,
                "image": Image.open(image).resize((768, 768)),
                "negative_prompt": n_prompt,
                "num_inference_steps": num_inf_steps,
                "guidance_scale": g_scale,
                "image_guidance_scale": img_g_scale,
            },
            "postprocess": lambda r: r["images"][0],
        }
    if is_diffusers_pipeline_type(pipeline, "StableDiffusionUpscalePipeline"):
        return {
            "inputs": [
                components.Textbox(label="Prompt", render=False),
                components.Textbox(label="Negative prompt", render=False),
                components.Image(type="filepath", label="Image", render=False),
                components.Slider(
                    label="Number of inference steps",
                    minimum=1,
                    maximum=500,
                    value=50,
                    step=1,
                ),
                components.Slider(
                    label="Guidance scale",
                    minimum=1,
                    maximum=20,
                    value=7.5,
                    step=0.5,
                ),
                components.Slider(
                    label="Noise level", minimum=1, maximum=100, value=20, step=1
                ),
            ],
            "outputs": components.Image(
                label="Generated Image", render=False, type="pil"
            ),
            "preprocess": lambda prompt,
            n_prompt,
            image,
            num_inf_steps,
            g_scale,
            noise_level: {
                "prompt": prompt,
                "image": Image.open(image).resize((768, 768)),
                "negative_prompt": n_prompt,
                "num_inference_steps": num_inf_steps,
                "guidance_scale": g_scale,
                "noise_level": noise_level,
            },
            "postprocess": lambda r: r["images"][0],
        }
    raise ValueError(f"Unsupported diffusers pipeline type: {type(pipeline)}")


def handle_transformers_js_pipeline(pipeline: Any) -> Dict[str, Any]:
    try:
        from transformers_js_py import as_url
    except ImportError as ie:
        raise ImportError(
            "transformers_js_py not installed. Please add `transformers_js_py` to the requirements option of your Gradio-Lite app"
        ) from ie

    # if pipeline.task == "audio-classification":
    #     pass
    # if pipeline.task == "automatic-speech-recognition":
    #     pass
    # if pipeline.task == "depth-estimation":
    #     pass
    if pipeline.task == "document-question-answering":
        return {
            "inputs": [
                components.Image(type="filepath", label="Input Document", render=False),
                components.Textbox(label="Question", render=False),
            ],
            "outputs": components.Textbox(label="Label", render=False),
            "preprocess": lambda img, q: (as_url(img), q),
            "postprocess": lambda r: r[0][
                "answer"
            ],  # This data structure is different from the original Transformers.
        }
    if pipeline.task == "feature-extraction":
        return {
            "inputs": components.Textbox(label="Input", render=False),
            "outputs": components.Dataframe(label="Output", render=False),
            "preprocess": None,
            "postprocess": lambda tensor: tensor.to_numpy(),
        }
    if pipeline.task == "fill-mask":
        return {
            "inputs": components.Textbox(label="Input", render=False),
            "outputs": components.Label(label="Classification", render=False),
            "preprocess": None,
            "postprocess": lambda r: {i["token_str"]: i["score"] for i in r},
        }
    if pipeline.task == "image-classification":
        return {
            "inputs": [
                components.Image(type="filepath", label="Input Image", render=False),
                components.Number(label="Top k", value=5, render=False),
            ],
            "outputs": components.Label(label="Classification", render=False),
            "preprocess": lambda image_path, topk: (as_url(image_path), {"topk": topk}),
            "postprocess": lambda result: {
                item["label"]: item["score"] for item in result
            },
        }
    if pipeline.task == "image-segmentation":
        return {
            "inputs": components.Image(
                type="filepath", label="Input Image", render=False
            ),
            "outputs": components.AnnotatedImage(label="Segmentation", render=False),
            "preprocess": lambda image_path: (as_url(image_path),),
            "postprocess": lambda result, image_path: (
                image_path,
                [
                    (
                        item["mask"].to_numpy()[:, :, 0]
                        / 255.0,  # Reshape ([h,w,1] -> [h,w]) and normalize ([0,255] -> [0,1])
                        f"{item['label']} ({item['score']})",
                    )
                    for item in result
                ],
            ),
            "postprocess_takes_inputs": True,
        }
    # if pipeline.task == "image-to-text":
    #     pass
    if pipeline.task == "object-detection":
        return {
            "inputs": components.Image(
                type="filepath", label="Input Image", render=False
            ),
            "outputs": components.AnnotatedImage(
                label="Objects Detected", render=False
            ),
            "preprocess": lambda image_path: (as_url(image_path),),
            "postprocess": lambda result, image_path: (
                image_path,
                [
                    (
                        (
                            int(item["box"]["xmin"]),
                            int(item["box"]["ymin"]),
                            int(item["box"]["xmax"]),
                            int(item["box"]["ymax"]),
                        ),
                        f"{item['label']} ({item['score']})",
                    )
                    for item in result
                ],
            ),
            "postprocess_takes_inputs": True,
        }

    if pipeline.task == "question-answering":
        return {
            "inputs": [
                components.Textbox(lines=7, label="Context", render=False),
                components.Textbox(label="Question", render=False),
            ],
            "outputs": [
                components.Textbox(label="Answer", render=False),
                components.Label(label="Score", render=False),
            ],
            "preprocess": lambda c, q: (
                q,
                c,
            ),  # Placed the context first in the input UI to match `handle_transformers_pipeline`'s order of inputs, but Transformers.js' question-answering pipeline expects the question first.
            "postprocess": lambda r: (r["answer"], r["score"]),
        }
    if pipeline.task == "summarization":
        return {
            "inputs": [
                components.Textbox(lines=7, label="Input", render=False),
                components.Slider(
                    label="The maximum numbers of tokens to generate",
                    minimum=1,
                    maximum=500,
                    value=100,
                    step=1,
                    render=False,
                ),
            ],
            "outputs": components.Textbox(label="Summary", render=False),
            "preprocess": lambda text, max_new_tokens: (
                text,
                {"max_new_tokens": max_new_tokens},
            ),
            "postprocess": lambda r: r[0]["summary_text"],
        }
    if pipeline.task == "text2text-generation":
        return {
            "inputs": [
                components.Textbox(label="Input", render=False),
                components.Slider(
                    label="The maximum numbers of tokens to generate",
                    minimum=1,
                    maximum=500,
                    value=100,
                    step=1,
                    render=False,
                ),
            ],
            "outputs": components.Textbox(label="Generated Text", render=False),
            "preprocess": lambda text, max_new_tokens: (
                text,
                {"max_new_tokens": max_new_tokens},
            ),
            "postprocess": lambda r: r[0]["generated_text"],
        }
    if pipeline.task == "text-classification":
        return {
            "inputs": [
                components.Textbox(label="Input", render=False),
                components.Number(label="Top k", value=5, render=False),
            ],
            "outputs": components.Label(label="Classification", render=False),
            "preprocess": lambda text, topk: (text, {"topk": topk}),
            "postprocess": lambda r: {i["label"]: i["score"] for i in r},
        }
    if pipeline.task == "text-generation":
        return {
            "inputs": components.Textbox(label="Input", render=False),
            "outputs": components.Textbox(label="Output", render=False),
            "preprocess": None,
            "postprocess": lambda r: r[0]["generated_text"],
        }
    # if pipeline.task == "token-classification":
    #     pass
    if pipeline.task in {"translation", "translation_xx_to_yy"}:
        return {
            "inputs": [
                components.Textbox(label="Input", render=False),
                components.Textbox(label="Source Language", render=False),
                components.Textbox(label="Target Language", render=False),
            ],
            "outputs": components.Textbox(label="Translation", render=False),
            "preprocess": lambda x, s, t: (x, {"src_lang": s, "tgt_lang": t}),
            "postprocess": lambda r: r[0]["translation_text"],
        }
    if pipeline.task == "zero-shot-classification":
        return {
            "inputs": [
                components.Textbox(label="Input", render=False),
                components.Textbox(
                    label="Possible class names (comma-separated)", render=False
                ),
            ],
            "outputs": components.Label(label="Classification", render=False),
            "preprocess": lambda text, classnames: (
                text,
                [c.strip() for c in classnames.split(",")],
            ),
            "postprocess": lambda result: dict(zip(result["labels"], result["scores"])),
        }
    # if pipeline.task == "zero-shot-audio-classification":
    #     pass
    if pipeline.task == "zero-shot-image-classification":
        return {
            "inputs": [
                components.Image(type="filepath", label="Input Image", render=False),
                components.Textbox(
                    label="Possible class names (comma-separated)", render=False
                ),
            ],
            "outputs": components.Label(label="Classification", render=False),
            "preprocess": lambda image_path, classnames: (
                as_url(image_path),
                [c.strip() for c in classnames.split(",")],
            ),
            "postprocess": lambda result: {i["label"]: i["score"] for i in result},
        }
    if pipeline.task == "zero-shot-object-detection":
        return {
            "inputs": [
                components.Image(type="filepath", label="Input Image", render=False),
                components.Textbox(
                    label="Possible class names (comma-separated)", render=False
                ),
            ],
            "outputs": components.AnnotatedImage(
                label="Objects Detected", render=False
            ),
            "preprocess": lambda image_path, classnames: (
                as_url(image_path),
                [c.strip() for c in classnames.split(",")],
            ),
            "postprocess": lambda result, image_path, _: (
                image_path,
                [
                    (
                        (
                            int(item["box"]["xmin"]),
                            int(item["box"]["ymin"]),
                            int(item["box"]["xmax"]),
                            int(item["box"]["ymax"]),
                        ),
                        f"{item['label']} ({item['score']})",
                    )
                    for item in result
                ],
            ),
            "postprocess_takes_inputs": True,
        }

    raise ValueError(f"Unsupported transformers pipeline type: {pipeline.task}")
