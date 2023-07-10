#!/usr/bin/env python3
"""A module to measure total execution time for a function"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """The implementation of the function"""
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed/n
