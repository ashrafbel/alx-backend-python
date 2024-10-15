#!/usr/bin/env python3
"Tasks"

import asyncio
from typing import List
from random import uniform

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Run several coroutines concurrently using async.
    Args:
        n (int): The number of times to execute wait_random.
    Returns:
        List[float]: A list of delays sorted in ascending order.
    """
    delays = []
    tasks = []
    for _ in range(n):
        t = task_wait_random(max_delay)
        tasks.append(t)
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
