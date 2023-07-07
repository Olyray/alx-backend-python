#!/usr/bin/env python3
"""A function that returns a function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return the function"""
    return lambda x: x * multiplier
