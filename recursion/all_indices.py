#!/bin/python3
# -*- coding: utf-8 -*-

from typing import Iterable

def indices(string: str, character: str, i: int = 0) -> Iterable:
    """Recursive generator to find and return all indices of
    a string for a given character.
    
    Parameters
    ----------
    string : str
        Main character array to search for character indices.
    character : str
        Target character for which to find and return indices.

    Returns
    -------
    Iterable
        Generator object that will "walk" to each index match and
        return that value.

    Examples -
    >>> sample = "a-b-c-d"
    >>> list(indices(sample, "-"))
    [1, 3, 5]
    >>> sample = "a-bb-ccc-ddd-"
    >>> list(indices(sample, "-"))
    [1, 4, 8, 12]   
    >>> sample = ""
    >>> list(indices(sample, "-"))
    []
    >>> sample = "4"
    >>> list(indices(sample, "-"))
    []
    >>> list(indices(None, "-"))
    []
    """

    if string:
        match_idx = string.find(character, i)

        # str.find() returns -1 if not match found, so
        # exit function if that is the case.
        if match_idx < 0:
            return

        # Increment i by matched index plus one.
        i = match_idx + 1

        # Yield match result
        yield match_idx

        # Yield from function with updated parameters.
        yield from indices(string, character, i)
    return


if __name__ == "":
    import doctest
    doctest.testmod()
