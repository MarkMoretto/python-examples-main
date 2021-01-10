
"""
Purpose: 
Date created: 2020-07-25

URL: https://stackoverflow.com/questions/63092491/find-number-of-sublists-in-list-of-many-lists/63092618#63092618

My solution: https://stackoverflow.com/a/63092618/2847946

Contributor(s):
    Mark M.
"""


xyz = [[[
        [-1.241956526315958, 54.722452909315834],
        [-1.242505189342398, 54.72242038994674],
        [-1.24192061729046, 54.722713302903806],
        [-1.241956526315958, 54.722452909315834]]],
    [[[-1.270237428346303, 54.7271584144655],
      [-1.268210325997062, 54.72608036652354],
      [-1.267390512992676, 54.726854573664205]]]]

abc = [[[0.35734960034587, 51.691419401103474], [0.360525134769747, 51.69037987969592], [0.362860024738573, 51.69170434483416]]]


# def flatten(iterable):
#     """Recursive flattening of sublists."""
#     if len(iterable) > 1:
#         res = flatten(iterable[0])
#     else:
#         res = iterable[0]
#     return res

def flatten(iterable):
    """Recursive flattening of sublists."""

    if len(iterable) > 1:
        res = flatten(iterable[0])
    else:
        res = iterable[0]

    return res



def flatten(iterable):
    """Recursive flattening of sublists."""
    for el in iterable:
        return flatten(el)
    else:
        return flatten(iterable)

# flatten(abc)

def coord_pairs(lists):
    out = ""
    if len(lists) > 1:
        for item in lists:
            res = flatten(item)
            out += ":".join([f"{c[1]},{c[0]}" for c in res])
    else:
        res = flatten(lists)
        out += ":".join([f"{c[1]},{c[0]}" for c in res])
    return out



# def coord_pairs(coordinates):
#     """Returns coordinate pairs from list of coordinates."""
#     coords = flatten(coordinates)
#     return ":".join([f"{c[1]},{c[0]}" for c in coords])


coord_pairs(xyz)


# Lambda flattening.
flattener = lambda lst: [i for e in lst for i in (flattener(e) if isinstance(e, list) else [e])]




coord_pairs(abc)


# def flatten(iterable):
#     """Recursive flattening of sublists."""
#     if len(iterable) > 1:
#         res = flatten(iterable[0])
#     else:
#         res = iterable[0]
#     return res


# def coord_pairs(lists):
#     out = ""
#     for item in lists:
#         res = flatten(item)
#         out += ":".join([f"{c[1]},{c[0]}" for c in res])
#     return out
