#!/usr/bin/env python3
"""Module defines sum_mixed_list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return sum of mixed list as float"""
    return float(sum(mxd_lst))
