from monai.utils import optional_import
from typing import Union, Sequence, Hashable, Collection
from monai.utils import Method, NumpyPadMode
from monai.config import IndexSelection, KeysCollection
from monai.config.type_definitions import NdarrayOrTensor

import numpy as np 
import torch

pytest, has_pytest = optional_import("pytest")

from ..Utils.function_phaser import phase_arguments


def test_general_function_parsing():

    def target_func(arg_1: int, arg_2: bool, arg_3: str = "hello"):
        pass
    
    expected = {
        'arg_1': {'type': int, 'default': None, 'is_optional': True, 'candidates': []}, 
        'arg_2': {'type': bool, 'default': None, 'is_optional': True, 'candidates': []},
        'arg_3': {'type': str, 'default': 'hello', 'is_optional': False, 'candidates': []}
    }

    ret = phase_arguments(target_func)
    assert ret == expected


def test_monai_function_parsing():

    def target_func(
        arg_1: KeysCollection,
        arg_2: NdarrayOrTensor,
        arg_3: Union[Sequence[int], int],
        arg_4: Union[NumpyPadMode, str] = NumpyPadMode.CONSTANT,
        arg_5: Union[Method, str] = Method.SYMMETRIC,
    ):
        pass
    
    expected = {
        'arg_1': {'type': (Collection[Hashable], Hashable), 'default': None, 'is_optional': True, 'candidates': []}, 
        'arg_2': {'type': (np.ndarray, torch.Tensor), 'default': None, 'is_optional': True, 'candidates': []}, 
        'arg_3': {'type': (Sequence[int], int), 'default': None, 'is_optional': True, 'candidates': []},
        'arg_4': {'type': (NumpyPadMode, str), 'default': NumpyPadMode.CONSTANT, 'is_optional': False, 'candidates': ['CONSTANT', 'EDGE', 'LINEAR_RAMP', 'MAXIMUM', 'MEAN', 'MEDIAN', 'MINIMUM', 'REFLECT', 'SYMMETRIC', 'WRAP', 'EMPTY']},
        'arg_5': {'type': (Method, str), 'default': Method.SYMMETRIC, 'is_optional': False, 'candidates': ['SYMMETRIC', 'END']}}

    ret = phase_arguments(target_func)
    assert ret == expected


