#!/usr/bin/env python3
'Measure the runtime'


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total runtime for executing wait_n(n, max_delay).
    Args:
        n (int): Number of times to call wait_random.
        max_delay (int): Maximum delay in seconds for wait_random.
    Returns:
        float: Average runtime per wait_random call.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total = end - start
    return total / n
