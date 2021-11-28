#!/bin/python3
# -*- coding: utf-8 -*-

"""Rank integer list items by relative standing.


See: https://stackoverflow.com/questions/21220150/rank-the-suffixes-of-a-list
"""

def filterer(target: int, iterable: tuple, __cache={}):
    """Returns list of items that exclude the target item.
    
    Parameters
    ----------
    target : int
        Integer value to use in current evaluation.
    iterable : list
        Iterable to filter based on target item.

    Returns
    -------
    list
        Filtered list of items from original list.  Should exclude target value.
    """
    # Create immutable hash for referencing
    _hash = hash(tuple([target] + iterable))

    # Check if hash exists.  If not, create an entry.
    if not _hash in __cache:
        __cache[_hash] = list(filter(lambda n, t = target: n != t, iterable))
    return __cache[_hash]

 
def relative_rank(item_list: list, suffix: bool = True) -> list:
    """Return rank of items in list based on count of elements strictly less than (suffix)
    or strictly greater than (prefix) the current element.

    >>> a = [51, 38, 29, 51, 63, 38]
    >>> relative_rank(a)
    [3, 1, 0, 3, 5, 1]
    >>> relative_rank(a, suffix = False)
    [1, 3, 5, 1, 0, 3]
    """

    def __quantify(pred: bool, iterable: list):
        """Return sum (count) of positive results based on given predicate applied to
        an iterable collection.
        """
        return sum(map(pred, iterable))

    # Prefix and suffix functions.
    def suffix_quantify(target: int, iterable: list) -> int:
        return __quantify(lambda h: h < target, iterable)

    def prefix_quantify(target: int, iterable: list) -> int:
        return __quantify(lambda h: h > target, iterable)

    # Set function based on suffix argument
    if suffix:
        fn_quantify = suffix_quantify
    else:
        fn_quantify = prefix_quantify
    

    # Filter list for items not currently the target item.
    output = {}
    for el in set(item_list):

        # sm_list = list(filter(lambda n, t = el: n != t, item_list))
        fewer_items = filterer(el, item_list)

        q = fn_quantify(el, fewer_items)

        print(fewer_items, q)

        output[el] = q
        # output.append(q)

    # Return mapped quantity results. Returns zero if item missing.
    return [output.get(n, 0) for n in item_list]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
