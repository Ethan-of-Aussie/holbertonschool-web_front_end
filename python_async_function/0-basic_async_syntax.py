#!/usr/nin/env python3
"""Module defines wait_random"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine, that waits for a random delay between 0 and max_delay"""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
