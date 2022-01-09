#!/bin/python

from __future__ import annotations

def is_number(s: str) -> bool:
    """ Returns True is string is a number, else False.
    """
    return s.replace(".", "",1).isdigit()


def is_float(s: str) -> bool:
    """Returns True if string represents floating-point number, else False.
    """
    try:
        float(s)
        return True
    except ValueError:
        return False

    
def size(number: (int | float), __size: int = 0) -> int:
    """Return count of digits in decimal number.  This does not return
    the number of bits or memory allocation to the variable.

    Parameters
    ----------
    number : int
        Decimal number to process.

    Returns
    -------
    int
        Size of decimal number (how many digits it has).  If non numeric value
        passed, then -1 will be returned.

    Examples
    --------
    >>> size(1111)
    4
    >>> size("1111")
    4
    >>> size(-1111)
    4
    >>> size("abcd")
    -1
    >>> size("")
    -1
    """

    def _sz(n, i: int = 0) -> int:
        """Inner function that calculates size of numeric value."""
        if n:
            return _sz(n//10, i+1)
        return i

    if isinstance(number, str) and is_number(number):
        if is_float(number):
            number = float(number)
        else:
            number = int(number)
        
    if isinstance(number, (int, float)):
        # Use abs() to handle negative values.
        return _sz(abs(number))
    
    else:
        return -1


if __name__ == "__main__":
    import doctest
    doctest.testmod()

