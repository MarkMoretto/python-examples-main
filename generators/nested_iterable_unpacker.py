
"""
Purpose: Recursive unpacking of nested lists.
Date created: 2020-12-28

Ref:
    https://stackoverflow.com/a/65485250/2847946

Contributor(s):
    nilo <https://stackoverflow.com/users/3246135/nilo>
    Mark M.
"""


def unpack_nested_iterable(data):
    while True:
        head, *tail = data if data else (None,)
        try:
            # Can we go deeper?
            len(head)
        except TypeError:
            # Deepest level
            yield list(data)
            return
        yield tail
        data = head

def correct_order(iterable):
    unpacked_iter = list(unpack_recursive_iterable(iterable))
    if "reverse" in dir(unpacked_iter):
        unpacked_iter.reverse()
    else:
        unpacked_iter = unpacked_iter[::-1]
    return unpacked_iter

data1 = (((1, 2, 3, 4), 5, 6, 7, 8), 9, 10, 11, 12)
res1 = [o for o in unpack_nested_iterable(data1)]
print(res1)

