#!/usr/bin/env python3
"""A function that returns the sum of a mixed list of integers and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum"""
    return sum(mxd_lst)
