#!/bin/python
"""Function to convert camelCase to snake_case.
"""

import re

try:
    from functools import cache
except ModuleNotFoundError as e:
    from functools import lru_cache as cache

@cache
def camel_to_snake(string: str, _p = re.compile(r"""(?<=[a-z0-9])([A-Z])""")) -> str:
    """Return text converted from camelCase to snake_case.  This will not insert underscores by inference, so those should be added
    to a string prior to running the function.

    Examples
    --------
    >>> camel_to_snake("publicId")
    public_id
    >>> camel_to_snake("publicid")
    publicid
    >>> camel_to_snake("public_id")
    public_id
    >>> camel_to_snake("PublicId")
    public_id
    >>> camel_to_snake("Id")
    publicid
    """
    return _p.sub(r"_\1", string).lower()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
