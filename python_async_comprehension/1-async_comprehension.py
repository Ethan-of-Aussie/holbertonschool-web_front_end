#!/usr/bin/env python3
"""Defines async_comprehension, used to display async comprehension"""


from typing import List
import asyncio, random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Returns the random numbers of async_generator"""
    return [i async for i in async_generator()]