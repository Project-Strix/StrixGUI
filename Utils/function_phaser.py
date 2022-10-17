from typing import Union, TypeVar, get_args, get_origin
import inspect
from monai.utils import enums


def phase_arguments(func, phase_all_args: bool = True):
    """Phase function's arguments and return a structured dict.

    Args:
        func: Target function.
        phase_all_args (bool, optional): whether to phase all arguments.
            If False, phaser will skip arguments with default value given. Defaults to True.

    Returns:
        dict: a structured arguments dict.
    """
    sig = inspect.signature(func)
    anno = inspect.getfullargspec(func).annotations
    if not phase_all_args:
        cond = lambda x: x[1].default is x[1].empty
    else:
        cond = lambda x: True

    def _parse(arg_name, argument_types, default_value, is_optional):
        results = {}
        candidate = []
        if isinstance(argument_types, (tuple, list)):
            for arg_type in argument_types:
                if hasattr(arg_type, '__name__') and arg_type.__name__ in enums.__all__:
                    candidate += list(arg_type.__members__.keys())
        
        return {
            arg_name: 
                {
                    "type": argument_types,
                    "default": default_value,
                    "is_optional": (default_value is None) or is_optional,
                    "candidates": candidate
                }
        }

    arguments = {}
    for k, v in filter(cond, sig.parameters.items()):
        args = anno.get(k)
        is_optional = False
        default_value = None if v.default is v.empty else v.default
        if get_origin(args) is Union:
            args = get_args(args)
            if args:
                if type(None) in args:  # it's optional
                    args = tuple(item for item in args if item != type(None))
                    is_optional = True
        elif get_origin(args) is TypeVar:
            args = get_args(args)

        arguments.update(_parse(k, args, default_value, is_optional))

    return arguments