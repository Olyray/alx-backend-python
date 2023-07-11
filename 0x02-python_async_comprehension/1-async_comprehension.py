#!/usr/bin/env python3
"""A module to use async comprehensions"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Implementation of the async comprehension"""
    return [result async for result in async_generator()]
