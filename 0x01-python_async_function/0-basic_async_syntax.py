#!/usr/bin/env python3
"""A function that uses async to return a time delay"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Implementation of the function"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
