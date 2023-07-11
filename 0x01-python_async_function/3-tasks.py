#!/usr/bin/env python3
"""A module to create a task from a coroutine function"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function to create the task"""
    return asyncio.create_task(wait_random(max_delay))
