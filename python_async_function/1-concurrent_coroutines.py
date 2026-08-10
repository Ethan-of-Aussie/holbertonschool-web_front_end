#!/usr/bin/env python3
"""Defines async function to spawn n times with float wait_random into sorted list"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def insertion_sort(lst):
    """Sort a list of floats in ascending order using insertion sort."""
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times and return sorted delays."""
    tasks = [asyncio.create_task(wait_random(max_delay))for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return insertion_sort(delays)
    