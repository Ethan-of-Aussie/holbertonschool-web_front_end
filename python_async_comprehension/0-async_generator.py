#!/usr/bin/env python3
"""Defines function async generator"""


import random, asyncio

async def async_generator():
    """Between 0 to 10, Numbers are generated and waited per loop"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
