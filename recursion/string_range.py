
"""
Purpose: 
Date created: 2021-08-08

Contributor(s):
    Mark M.
"""


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Iterator


def srange(start: int, stop: int = None, step: int = 1) -> Iterator:
    """Simple recursive generator that returns numeric values as a string type.
    Should be a drop-in replacement for the built-in `range()` function in 
    Python 3.x.  From that documentation:
    
    "Return an object that produces a sequence of integers from start (inclusive) 
    to stop (exclusive) by step. range(i, j) produces i, i+1, i+2, ..., j-1. start
    defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.  These are
    exactly the valid indices for a list of 4 elements."
    
    "When step is given, it specifies the increment (or decrement)."
    
    Parameters
    ----------
    start: int
    If stop is given, this is the starting value (inclusive) for the output of a range of
    values. Otherwise, this will be the stop value (exclusive).
    stop: int
    Max value to return (exclusive).  Default: None.
    step: int
    Total numbers that should be skipped when producing a range of results.  Default: 1.
    >>> list(srange(10))
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    >>> list(srange("10"))
    Traceback (most recent call last):
            ...
    TypeError: '<' not supported between instances of 'int' and 'str'
    """


    if stop is None:
        stop = start
        start = 0
		
    if start < stop:
        yield f"{start}"
        yield from srange(start + step, stop, step)


if __name__ == "__main__":
	import doctest
	doctest.testmod()
