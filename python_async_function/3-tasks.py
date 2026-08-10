#!/usr/bin/env python3
"""Module that define task_wait_random as non-async function"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """None async function that takes a int and returns asyncio.Task"""
    return asyncio.Task(wait_random(max_delay))
