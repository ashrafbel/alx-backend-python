#!/usr/bin/env python3
"The basics of async"


from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    "return list of ordered delays"
    delays = []
    for _ in range(n):
        d = await wait_random(max_delay)
        delays.append(d)
    return sorted(delays)
