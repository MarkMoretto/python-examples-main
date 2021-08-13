
from typing import Iterator

# Create decimal-to-hexadecimal map.
hexmap = {i:str(i) for i in range(0, 10)}
hexmap.update(dict(zip(range(10, 16), list("abcdef"))))


def hexcursion(val: int) -> Iterator:
    """Generator that returns base 16 values of a given decimal number.
    
    Parameters
    ----------
    val : int
        Decimal value to convert to hexadecimal.

    Returns
    -------
    Iterator

    >>> dec_value = 4253
    >>> list(hexcursion(dec_value))
    ['d', '9', '0', '1']

    """
    if val > 0:
        rem = val % 16
        yield hexmap[rem]
        yield from hexcursion(val // 16)
    return


def get_hex(decimal_: int) -> str:
    """Return hexadecimal value of a decimal number.

    Parameters
    ----------
    decimal_ : int
        Decimal value to convert to hexadecimal.

    Returns
    -------
    str
        Decimal number as hexadecimal value.

    >>> dec_value = 4253
    >>> get_hex(dec_value)
    '109d'
    >>> get_hex("1234")
    Traceback (most recent call last):
        ...
    TypeError: '>' not supported between instances of 'str' and 'int'
    """
    return "".join(list(hexcursion(decimal_))[::-1])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
