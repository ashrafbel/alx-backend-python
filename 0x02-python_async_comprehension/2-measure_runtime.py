#!/usr/bin/env python3
"Run time for four parallel comprehensions"

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    "Coroutine runs async_comprehension 4 in parallel and returns runtime"
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    t = time.time() - start
    return t
