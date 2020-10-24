# -*- coding: utf-8 -*-
"""
Created on 2020-10-09

https://www.codewars.com/kata/5b5fe164b88263ad3d00250b

@author: mark.moretto

Desc - 

    Alphametics is a type of cryptarithm in which a set of words is written down in the
    form of a long addition sum or some other mathematical problem. The objective is to
    replace the letters of the alphabet with decimal digits to make a valid arithmetic sum.
    
    For this kata, your objective is to write a function that accepts an alphametic
    equation in the form of a single-line string and returns a valid arithmetic equation
    in the form of a single-line string.
"""

# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# sample = "SEND + MORE = MONEY"
# equation, solution = sample.split(" = ")
# lhs = equation.split(" + ")
# ssample = sample.replace("=", "==") #Equality checker
# unique_words = set(lhs)
# unique_letters = set("".join(unique_words)+solution)
# keymap = dict.fromkeys(unique_letters, nums)
# used_nums = dict.fromkeys(unique_letters, [])

"""
{'Y': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 'O': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 'M': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 'R': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 'E': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 'S': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 'N': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
 'D': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}
"""
def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)
            

        
    
rng = "".join(map(str, range(10)))

sample = "SEND + MORE = MONEY"

equation, solution = list(map(str.strip, sample.split("=")))

words = list(map(str.strip, equation.split("+")))

unique_words = set(words)

unique_letters = sorted(set("".join(unique_words)+solution))

unique_len = len(unique_letters)

# Unique first letter for the string
first_letters = [w[0] for w in unique_words]
# Number of unique first letters
n_firsts = first_letters.__len__()

# Letters arranged so that unique first letters are at the start.
chars = "".join(first_letters)
chars += "".join(set(unique_letters).difference(first_letters))



for perm in permutations(rng, unique_len):
    if not "0" in perm[:n_firsts]:
        tdict = str.maketrans(chars, "".join(perm))
        L = sum(map(lambda s: int(s.translate(tdict)), words))
        R = solution.translate(tdict)
        if L == R:
            print(f"solution found for {tdict}")
            break
