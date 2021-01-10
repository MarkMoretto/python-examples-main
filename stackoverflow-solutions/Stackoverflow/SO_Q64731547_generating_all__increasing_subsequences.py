
"""
Purpose: Generating all the increasing subsequences
Date created: 2020-11-07

https://stackoverflow.com/questions/64731547/generating-all-the-increasing-subsequences

Contributor(s):
    Mark M.
"""


from itertools import combinations
import itertools as ittr


sample = [1, 2, 4, 5, 3, 6]

[ all(map(lambda x: x[0]< x[1], zip(sample[:-1], sample[1:])))

results = []
for j, comb in enumerate(combinations(sample, 4)):
    results = sorted(results)
    if j == 0:
        results.append(comb)
    else:
        i = 1
        counter = 0
        while i < 4:
            a, b = comb[i-1], comb[i]
            if a < b:
                counter += 1
            i += 1
        if counter == 3:
            if all(map(lambda x: x[0] < x[1], zip(results[j-1], comb))):
                results.append(comb)
        print(comb)


"""
list(map(lambda c: sum([1 for i in range(1, 4) if c[i-1]<c[i]]), combinations(sample, 4)))

list(val for _, val in ittr.takewhile(lambda i_val: i_val[0] < n, enumerate(generator)))


ittr.takewhile(lambda q: q == 3, list(map(lambda c: sum([1 for i in range(1, 4) if c[i-1]<c[i]]), combinations(sample, 4))))

zeta=[(1,1),(2,2),(4,3),(5,4),(3,5),(6,6)]



comb=combinations(zeta,4)
list(comb)
list(map(lambda c: sum([1 for i in range(1, 4) if c[i-1]<c[i]]), combinations(sample, 4)))

comb=combinations(sorted(zeta,key=lambda x:x[0]),4)
def verif(x):
    l=[]
    for k in x :
        l.append(k[1])
    for i in range(len(l)-1):
        if l[i+1]-l[i] < 0 : return 0
    return 1

for i in comb:
    if verif(list(i)):
        print(i)


# ((1, 1), (2, 2), (3, 5), (6, 6))
# ((1, 1), (2, 2), (4, 3), (5, 4))
# ((1, 1), (2, 2), (4, 3), (6, 6))
# ((1, 1), (2, 2), (5, 4), (6, 6))
# ((1, 1), (4, 3), (5, 4), (6, 6))
# ((2, 2), (4, 3), (5, 4), (6, 6))


combs = [((1, 1), (2, 2), (4, 3), (5, 4)),
 ((1, 1), (2, 2), (4, 3), (3, 5)),
 ((1, 1), (2, 2), (4, 3), (6, 6)),
 ((1, 1), (2, 2), (5, 4), (3, 5)),
 ((1, 1), (2, 2), (5, 4), (6, 6)),
 ((1, 1), (2, 2), (3, 5), (6, 6)),
 ((1, 1), (4, 3), (5, 4), (3, 5)),
 ((1, 1), (4, 3), (5, 4), (6, 6)),
 ((1, 1), (4, 3), (3, 5), (6, 6)),
 ((1, 1), (5, 4), (3, 5), (6, 6)),
 ((2, 2), (4, 3), (5, 4), (3, 5)),
 ((2, 2), (4, 3), (5, 4), (6, 6)),
 ((2, 2), (4, 3), (3, 5), (6, 6)),
 ((2, 2), (5, 4), (3, 5), (6, 6)),
 ((4, 3), (5, 4), (3, 5), (6, 6))]


t1 = ((1, 1), (2, 2), (4, 3), (5, 4))


results = []
for i, comb in enumerate(combinations(zeta, 4)):
    if i == 0:
        results.append(comb)
    else:
        tmp = []
        for j in range(1, 4):
            if comb[j-1][1] < comb[j][1]:
                tmp.append(comb[j][1])
        if len(tmp) == 3:
            results.append(comb)



def take_element(n, generator):
    list(val for _, val in ittr.takewhile(lambda i_val: i_val[0] < n, enumerate(generator)))
"""