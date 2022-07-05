"""
Defines helper methods useful for loading and caching Interface examples.
"""
from __future__ import annotations

import csv
import os
import shutil
from typing import TYPE_CHECKING, Any, Callable, List, Optional, Tuple

from gradio.components import Dataset
from gradio.flagging import CSVLogger

if TYPE_CHECKING:  # Only import for type checking (to avoid circular imports).
    from gradio import Interface
    from gradio.components import Component

CACHED_FOLDER = "gradio_cached_examples"


class Examples:
    def __init__(
        self,
        examples: List[Any] | List[List[Any]] | str,
        inputs: Component | List[Component],
        outputs: Optional[Component | List[Component]] = None,
        fn: Optional[Callable] = None,
        cache_examples: bool = False,
        examples_per_page: int = 10,
    ):
        """
        This class is a wrapper over the Dataset component can be used to create Examples
        for Blocks / Interfaces. Populates the Dataset component with examples and
        assigns event listener so that clicking on an example populates the input/output
        components. Optionally handles example caching for fast inference.

        Parameters:
        examples (List[Any] | List[List[Any]] | str): example inputs that can be clicked to populate specific components. Should be nested list, in which the outer list consists of samples and each inner list consists of an input corresponding to each input component. A string path to a directory of examples can also be provided.
        inputs: (Component | List[Component]): the component or list of components corresponding to the examples
        outputs: (Component | List[Component] | None): optionally, provide the component or list of components corresponding to the output of the examples. Required if `cache` is True.
        fn: (Callable | None): optionally, provide the function to run to generate the outputs corresponding to the examples. Required if `cache` is True.
        cache_examples (bool): if True, caches examples for fast runtime. If True, then `fn` and `outputs` need to be provided
        examples_per_page (int): how many examples to show per page (this parameter currently has no effect)
        """
        if not isinstance(inputs, list):
            inputs = [inputs]
        if not isinstance(outputs, list):
            outputs = [outputs]

        if examples is None:
            raise ValueError("The parameter `examples` cannot be None")
        elif isinstance(examples, list) and (
            len(examples) == 0 or isinstance(examples[0], list)
        ):
            pass
        elif (
            isinstance(examples, list) and len(inputs) == 1
        ):  # If there is only one input component, examples can be provided as a regular list instead of a list of lists
            examples = [[e] for e in examples]
        elif isinstance(examples, str):
            if not os.path.exists(examples):
                raise FileNotFoundError(
                    "Could not find examples directory: " + examples
                )
            log_file = os.path.join(examples, "log.csv")
            if not os.path.exists(log_file):
                if len(inputs) == 1:
                    exampleset = [
                        [os.path.join(examples, item)] for item in os.listdir(examples)
                    ]
                else:
                    raise FileNotFoundError(
                        "Could not find log file (required for multiple inputs): "
                        + log_file
                    )
            else:
                with open(log_file) as logs:
                    exampleset = list(csv.reader(logs))
                    exampleset = exampleset[1:]  # remove header
            for i, example in enumerate(exampleset):
                for j, (component, cell) in enumerate(
                    zip(
                        inputs + outputs,
                        example,
                    )
                ):
                    exampleset[i][j] = component.restore_flagged(
                        examples,
                        cell,
                        None,
                    )
            examples = exampleset
        else:
            raise ValueError(
                "The parameter `examples` must either be a directory or a nested "
                "list, where each sublist represents a set of inputs."
            )
            
        if cache_examples and (fn is None or outputs is None):
            raise ValueError("If caching examples, `fn` and `outputs` must be provided")
        
        dataset = Dataset(
            components=inputs,
            samples=examples,
            type="index",
        )

        self.examples = examples
        self.inputs = inputs
        self.outputs = outputs
        self.fn = fn
        self.cache_examples = cache_examples
        self.examples_per_page = examples_per_page
        self.cached_folder = os.path.join(CACHED_FOLDER, str(dataset._id))
        self.cached_file = os.path.join(self.cached_folder, "log.csv")

        if cache_examples:
            self.cache_interface_examples()

        def load_example(example_id):
            processed_examples = [
                component.preprocess_example(sample)
                for component, sample in zip(inputs, examples[example_id])
            ]
            if cache_examples:
                processed_examples += self.load_from_cache(example_id)
            if len(processed_examples) == 1:
                return processed_examples[0]
            else:
                return processed_examples

        dataset.click(
            load_example,
            inputs=[dataset],
            outputs=inputs + (outputs if cache_examples else []),
            _postprocess=False,
            queue=False,
        )

    def cache_interface_examples(self) -> None:
        """Caches all of the examples from an interface."""
        if os.path.exists(self.cached_file):
            print(
                f"Using cache from '{os.path.abspath(self.cached_folder)}' directory. If method or examples have changed since last caching, delete this folder to clear cache."
            )
        else:
            print(f"Caching examples at: '{os.path.abspath(self.cached_file)}'")
            cache_logger = CSVLogger()
            cache_logger.setup(self.outputs, self.cached_folder)
            for example_id, _ in enumerate(self.examples):
                try:
                    prediction = self.process_example(example_id)
                    cache_logger.flag(prediction)
                except Exception as e:
                    shutil.rmtree(self.cached_folder)
                    raise e

    def process_example(self, example_id: int) -> Tuple[List[Any], List[float]]:
        """Loads an example from the interface and returns its prediction."""
        example_set = self.examples[example_id]
        raw_input = [
            self.inputs[i].preprocess_example(example)
            for i, example in enumerate(example_set)
        ]
        processed_input = [
            input_component.preprocess(raw_input[i])
            for i, input_component in enumerate(self.inputs)
        ]
        predictions = self.fn(*processed_input)
        if len(self.outputs) == 1:
            predictions = [predictions]
        processed_output = [
            output_component.postprocess(predictions[i])
            if predictions[i] is not None
            else None
            for i, output_component in enumerate(self.outputs)
        ]

        return processed_output

    def load_from_cache(self, example_id: int) -> List[Any]:
        """Loads a particular cached example for the interface."""
        with open(self.cached_file) as cache:
            examples = list(csv.reader(cache, quotechar="'"))
        example = examples[example_id + 1]  # +1 to adjust for header
        output = []
        for component, cell in zip(self.outputs, example):
            output.append(
                component.restore_flagged(
                    self.cached_folder,
                    cell,
                    None,
                )
            )
        return output
