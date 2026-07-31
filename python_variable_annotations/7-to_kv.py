#!/usr/bin/env python3
"""Defines to_kv"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """"""
    return (k, float(v ** 2))