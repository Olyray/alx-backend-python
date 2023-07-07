#!/usr/bin/env python3
"""A function that returns a tuple of a float or int"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns the tuple"""
    return (k, v * v)
