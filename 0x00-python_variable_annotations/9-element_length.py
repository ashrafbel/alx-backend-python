#!/usr/bin/env python3
"type an iterable object"

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns:
    List[Tuple[Sequence, int]]: A list of tuples, where each tuple
    contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
