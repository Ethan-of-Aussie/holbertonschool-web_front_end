#!/usr/bin/env python3
"""Defines make_multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a multiplied multiplier by function multply"""
    def multply(val: float) -> float:
        return multiplier * val
    return multply