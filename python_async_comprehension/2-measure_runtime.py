#!/usr/bin/env python3
"""Defines async function measure_runtime"""

import asyncio, time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprhension in parallel four times"""
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )
    end = time.time()
    return end - start