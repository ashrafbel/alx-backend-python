#!/usr/bin/env python3
"Async Generator"
import asyncio
import random


async def async_generator():
    "Coroutine runs 10 times waits 1 second,yields random number from 0 to 10"
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
