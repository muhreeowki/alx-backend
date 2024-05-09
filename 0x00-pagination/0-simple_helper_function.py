#!/usr/bin/env python3
"""
Contains definition of index_range helper function
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes two integer arguments page and page_size.
    The function returns a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    """
    start, end = 0, 0
    for _ in range(page):
        start = end
        end += page_size

    return (start, end)
