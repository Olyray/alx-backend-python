#!/usr/bin/env python3
"""A module to asynchronously generate random numbers"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronously return ten random numbers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
