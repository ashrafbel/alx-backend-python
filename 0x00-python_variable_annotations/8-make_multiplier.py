#!/usr/bin/env python3
"Complex types - functions"
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    "returns the result of multiplying it by the multiplier"
    def multiply(number: float) -> float:
        " Multiply a number by the multiplier"
        return number * multiplier
    return multiply
