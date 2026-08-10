#!/usr/bin/env python3
"""Module contains async functions task_wait_n"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


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

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn task_wait_random n times and return sorted delays."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return insertion_sort(delays)
