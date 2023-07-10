#!/usr/bin/env python3
"""A module to execute multiple coroutines at the same time"""
import random
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes multiple coroutines"""
    list_of_delays = []
    # Create for loop n times:
    for i in range(n):
        # Use random.uniform with max_delay
        delay = random.uniform(0, max_delay)
        # Spawn wait random with the delay
        delay_result = await wait_random(delay)
        # Push the delay to the list
        list_of_delays.append(delay_result)
    # Return the list
    return sorted(list_of_delays)
