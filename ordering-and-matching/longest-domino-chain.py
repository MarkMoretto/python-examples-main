
"""
Purpose: Find longest chain of dominoes from given set.
Date created: 2020-01-14
Contributor(s): Mark Moretto

Ref URI: https://stackoverflow.com/questions/59726111/longest-domino-sequence

Note:
  Focus points would be:
    starting piece
    permutations
    greedy evaluation
    
"""

import re
from itertools import permutations as perms

sample_set = """
5
1 2
1 2
2 3
2 17
2 17
"""
sample_set = sample_set.strip()


dominoes = sample_set.split('\n')
n_dominoes = dominoes[0]
dominoes = dominoes[1:]


def pair_up(iterable):
    output = list()
    for i in iterable:
        a, b = re.split(r"\s+", i)
        output.append([a, b])
    return output

sets = pair_up(dominoes)

# For usage in SQL
def print_for_SQL():
    msg = """
    DROP TABLE IF EXISTS #_sets
    CREATE TABLE #_sets (
    	[set_id] INT IDENTITY(1,1) NOT NULL PRIMARY KEY
    	,	[side_a] VARCHAR(5)
    	,	[side_b] VARCHAR(5)
    )

    INSERT INTO #_sets
    """
    msg += "\n" + "VALUES " + ",\n".join([f"('{i[0]}','{i[1]}')" for i in sets])
    print(msg)
# print_for_SQL()

def unique_combos(n):
    return int((n * (n-1)) / 2)



def factorial(n):
    rng = [i * 1.0 for i in range(1, n + 1)]
    res = 1.0
    for i in rng:
        res *= i
    return res


def n_permutations(n, k):
    return factorial(n) / factorial(n-k)


p_sets_base = [[x for x in perms(i)] for i in sets]
p_sets = [i for i in perms(sets)]

max_len = len(sets) - 1
for idx, row in enumerate(p_sets[:5]):

    count = 0
    tmp = list()
    inv_row = [i[::-1] for i in row]

    for i, _ in enumerate(row):
        for j, _ in enumerate(inv_row):
            if i != j:
                if i < max_len and j < max_len:
                    print(row[i], row[i+1], inv_row[j], inv_row[j + 1])

        if i < max_len:
            left, right = row[i], row[i + 1]
            left_inv, right_inv = left[::-1], right[::-1]
            if i == 0:
                match_list_ct = list()
                match_list = list()
    
                if left[1] == right[0]:
                    match_list_ct.append(0)
                    match_list.append([left, right])
    
                elif left[1] == right_inv[0]:
                    match_list_ct.append(1)
                    match_list.append([left, right_inv])
    
                elif left_inv[1] == right[0]:
                    match_list_ct.append(2)
                    match_list.append([left_inv, right])
    
                elif left_inv[1] == right_inv[0]:
                    match_list_ct.append(3)
                    match_list.append([left_inv, right_inv])

                if len(match_list) > 0:
                    count += 1

            else

               if row[i][1] == row[i + 1][0]:
                   count += 1
                   tmp.append(row[i + 1])
               elif row[i][1] == row[i + 1][::-1][0]:
                   count += 1
                   tmp.append(row[i + 1][::-1])
       if count > 2:
           print(idx, " ", row)
           print(tmp)



def value_counts(iterable):
    all_values = [i for j in iterable for i in j]
    output_dict = {}
    for i in all_values:
        if not i in output_dict.keys():
            output_dict[i] = 1
        else:
            output_dict[i] += 1
    return output_dict
count_dict = value_counts(sets)
count_dict = dict(sorted(count_dict.items(), key = lambda x: x[1]))
min_numbers = [i for i in count_dict.keys() if count_dict[i] == min(count_dict.values())]
if len(min_numbers) == 1:
    min_domino = [i for i in sets if min_numbers[0] in i]
start_piece = min_domino[0]


set_dict = {k:v for k, v in enumerate(sets)}
dict_len = len(set_dict.keys())
chain_sets = {}
for k1 in range(dict_len):
    chain_sets[k1] = list()
    base = set_dict[k1]
    avail_keys = [k for k in set_dict.keys() if k != k1]
    counter = n_permutations(len(avail_keys), 2)
    while counter > 0.:
        for k2 in range(dict_len):
            if k1 != k2:
                base
                chain_sets[k1]
                print(f"{k1}:{iter_dict[k1]}\t{k2}:{iter_dict[k2]}")





tst1 = ['1', '2']
tst2 = ['1', '2']
def all_matches(a, b):
    b_inv = b[::-1]
    if a[1] == b[0]:
        return "First"
    elif a[1] == b[1]:
        return "Outside"
    elif a[1] == b_inv[0]:
        return "Insider"
    elif a[1] == b_inv[1]:
        return "Last"
    else:
        return None





# Left/right system?
set_dict = {k:v for k, v in enumerate(sets)}
dict_len = len(set_dict.keys())
counter = 0
while counter < dict_len:
    base = set_dict[counter]
    other = [v for k, v in set_dict.items() if k != counter]
    for pair in other:
        if base[0[ in pair or base[1] in pair:
            if
    print(base, "\t", other)
    counter += 1




chain_dict = dict()
for k1 in range(dict_len):
    base = set_dict[k1]
    chain_dict[k1] = [base]
    chain_list = [base]

    for k2 in range(dict_len):
        if k1 != k2:
            next_d = set_dict[k2]
            next_d_inv = next_d[::-1]
            if chain_list[-1][1] == next_d[0]:
                chain_list.append(next_d)
            elif chain_list[-1][1] == next_d_inv[0]:
                chain_list.append(next_d_inv)
    chain_dict[k1].append(chain_list)
