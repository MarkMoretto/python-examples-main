#!/bin/python

from __future__ import annotations
from typing import Any

def is_number(s: Any) -> bool:
    """Returns True if string is a number.
    """
    return str(s).replace(".", "",1).isdigit()

def size(number: int, __size: int = 0) -> int:
    """Return count of digits in decimal number.  This does NOT return
    the number of bits or memory allocation to the variable.

    Parameters
    ---------
    number : int
        Decimal number to process.

    Returns
    -------
    int
        Size of decimal number (how many digits it has).

    Example
    -------
    >>> a = 123
    >>> size(a)
    3
    >>> size("a")
    -1
    """

    # Check if value is numeric, then continue.
    if is_number(number):
        if number:
            return size(number//10, __size+1)
        return __size
    return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
