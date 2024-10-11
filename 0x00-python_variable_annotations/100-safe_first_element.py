#!/usr/bin/env python3
"first element of a sequence"
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    'return the first element of a list'
    if lst:
        return lst[0]
    else:
        return None
