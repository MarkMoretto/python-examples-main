
"""
Purpose: Stakcoverflow: sublists and ordered pairs

Date created: 2020-08-08

https://stackoverflow.com/questions/63321528/given-a-list-of-sublists-of-ordered-pairs-hops-how-can-i-count-the-number-of#63321528

Contributor(s):
    Mark M.
"""


pairs = [[(1,2), (3,3), (7,5)], [(2,3), (3,2), (6,4), (2,4)],]
# pairs = [[(1,2), (3,3), (7,5)], [(2,3), (3,2), (6,4), (2,4)], [(3,2), (2,4)],]

#flattener = lambda lst: [i for e in lst for i in (flattener(e) if isinstance(e, list) else [e])]

paths = [x for x in arr if x[0] == x[1]]

[f"{x}, {y}" for x in pairs[0] for y in pairs[1] if x[1] == y[0]]


[(x, y) for x in range(len(pairs)) for y in range(len(pairs)) if pairs[x][1] == pairs[y][0]]

def flatten(iterable):
    """Recursive flattening of sublists."""
    if isinstance(iterable, list):
        for el in iterable:
            return flatten(el)
        else:
            return flatten(iterable)
    else:
        return iterable

pairs = [[(1,2), (3,3), (7,5)], [(2,3), (3,2), (6,4), (2,4)], [(3,2), (2,4)],]

results = []
for x1 in range(len(pairs)):
    for y1 in range(len(pairs)):
        if y1 > x1:
            for x2 in range(len(pairs[x1])):
                for y2 in range(len(pairs[y1])):
                    if pairs[x1][x2][1] == pairs[y1][y2][0]:
                        results.extend([pairs[x1][x2], pairs[y1][y2]])

        if pairs[x][1] == pairs[y][0]:
            results.append([pairs[x][1], pairs[y][0]])






