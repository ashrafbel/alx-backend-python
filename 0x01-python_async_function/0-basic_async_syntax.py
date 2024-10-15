#!/usr/bin/env python3
"basics of async"

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    "Wait for a random delay between 0 and max_delay seconds"
    d = random.uniform(0, max_delay)
    await asyncio.sleep(d)
    return d
