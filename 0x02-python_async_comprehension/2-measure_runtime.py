#!/usr/bin/env python3
"""A module to execute an async comprehension in parralel"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """The implementation of the function"""
    start_count = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start_count
