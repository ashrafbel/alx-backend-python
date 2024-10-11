#!/usr/bin/env python3
"first element of a sequence"
from typing import Any, Optional


def safe_first_element(lst: list) -> Optional[Any]:
    'return the first element of a list'
    if lst:
        return lst[0]
    else:
        return None
