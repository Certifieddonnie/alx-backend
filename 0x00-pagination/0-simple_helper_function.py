#!/usr/bin/env python3
"""0-simple_helper_function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ returns a tuple of size two
    containing a start and end index
    """
    last = page * page_size
    first = last - page_size

    return (first, last)
