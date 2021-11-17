#!/bin/python3
# -*- coding: utf-8 -*-

from typing import Iterator

def triangle_num(value: int) -> int:
    """Returns triangular number for a given value.
    
    Parameters
    ----------
    value : int
        Integer value to use in triangular number calculaton.

    Returns
    -------
    int
        Triangular number.

    Examples:
    >>> triangle_num(0)
    0    
    >>> triangle_num(1)
    1
    >>> triangle_num(4)
    10
    >>> triangle_num(10)
    55
    >>> triangle_num("A")
    Traceback (most recent call last):
        ...
    TypeError: '>' not supported between instances of 'str' and 'int'
    >>> triangle_num(-1)
    Traceback (most recent call last):
        ...
    TypeError: Please use positive integer value   
    """
    if value >= 0:
        tot : list = [0]

        def recur(n: int, t: list) -> Iterator:
            if n > 0:
                t[0] += n
                n -= 1
                return recur(n, t)
            
        recur(value, tot)

        return tot[0]
    raise ValueError("Please use positive integer value.")
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
