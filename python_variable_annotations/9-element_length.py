#!/usr/bin/env python3
"""Defines element_length"""

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples containing each element and its length"""
    return [(i, len(i)) for i in lst]
