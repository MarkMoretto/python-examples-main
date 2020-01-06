
"""
Purpose: Ulam number algorithm
Date created: 2020-01-05

URI: https://en.wikipedia.org/wiki/Ulam_number

Contributor(s):
    Mark M.

From Wikipedia:

    An Ulam number is a member of an integer sequence devised by and named
    after Stanislaw Ulam, who introduced it in 1964.

    The standard Ulam sequence (the (1, 2)-Ulam sequence) starts with U1 = 1 
    and U2 = 2. Then for n > 2, Un is defined to be the smallest integer that
    is the sum of two distinct earlier terms in exactly one way and larger than
    all earlier terms.

    Terms must be distinct. For example, 4 is a member since:
        4 = 3 + 1

    But, we can ignore 2 + 2 since those aren't distinct values.
    
    We would skip 5 since it is representable in two ways
    5 = 1 + 4
    5 = 2 + 3

Notes:
    Wikipedia entry:
        https://en.wikipedia.org/wiki/Ulam_number

    OEIS entry and some script examples:
        https://oeis.org/A002858

    Wolfram entry:
        http://mathworld.wolfram.com/UlamSequence.html
"""



### First 60 verified results (n = 340)
### Per: https://oeis.org/A002858
valid_list = [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28, 36, 38, 47, 48, 53,
              57, 62, 69, 72, 77, 82, 87, 97, 99, 102, 106, 114, 126, 131,
              138, 145, 148, 155, 175, 177, 180, 182, 189, 197, 206, 209, 219,
              221, 236, 238, 241, 243, 253, 258, 260, 273, 282, 282, 309, 316,
              319, 324, 339]


#######################
### Final algorithm ###
def sequence_gen(current_n: int, iterable: list):
    sum_count: int = 0
    current_pair: tuple
    sum_count: int = 0
    for i in iterable:
        for j in iterable:
            if i < j:
                current_pair = sorted((j, i))
                if sum(current_pair) == current_n:
                    sum_count += 1
    if sum_count == 1:
        yield current_n


def ulam_sequence(n_digits: int) -> list:
    tmp: list
    n: int = 0
    ulam_digits: list = list()
    while n < n_digits:
        n += 1
        if n < 3:
            ulam_digits.append(n)
        else:
            tmp = [i for i in sequence_gen(n, ulam_digits)]
            if len(tmp) == 1:
                ulam_digits.append(n)
    return ulam_digits

##############################################################################
### Class format

class UlamSequence:
    def __init__(self, max_number: int):
        self.max_number = max_number
        self.ulam_digits: list = list()

    def __repr__(self):
        if self.max_number:
            return f"<Ulam Sequence class; max_number = {self.max_number}>"
        else:
            return f"<Ulam Sequence class>"

    @property
    def max_number(self) -> int:
        return self.__max_number

    @max_number.setter
    def max_number(self, value) -> None:
        if isinstance(value, int):
            self.__max_number = value
        else:
            raise ValueError("Please pase integer value for max_number.")

    def __ulam_generator(self) -> int:
        # current_pair: tuple
        sum_count: int = 0
        i: int
        j: int
        for i in self.ulam_digits:
            for j in self.ulam_digits:
                if i < j:
                    # Eval sum_count and break if >= 2 to save mem?
                    # current_pair = (i, j)
                    if sum((i, j)) == self.n:
                        sum_count += 1
        if sum_count == 1:
            yield 1


    def run(self) -> None:
        tmp: list
        self.ulam_digits: list = list()
        self.n: int = 0
        while self.n < self.max_number:
            self.n += 1
            if self.n < 3:
                self.ulam_digits.append(self.n)
            else:
                tmp = [i for i in self.__ulam_generator()]
                if len(tmp) == 1:
                    self.ulam_digits.append(self.n)
        if self.ulam_digits:
            return self.ulam_digits


## Samples
useq = UlamSequence(10)
res = useq.run()
print(res)

# Set new max_number and run
useq.max_number = 100
res = useq.run()
print(res)


# Set new max_number and run
useq.max_number = 100
res = useq.run()
print(res)



######################################################################
##########################################################################
##############################################################################
######### Work area
ulam_sequence(10)
ulam_sequence(100)
ulam_sequence(340)




sum_count: int # Aggregate count of sum of ulam numbers
current_pair: tuple
n_digits: int = 10

ulam_digits: list = [] # Keep a list of approved numbers


def sequence_gen(current_n: int, iterable: list):
    sum_count: int = 0
    current_pair: tuple
    sum_count: int = 0
    for i in iterable:
        for j in iterable:
            if i < j:
                current_pair = sorted((j, i))
                if sum(current_pair) == current_n:
                    sum_count += 1
                # print(f"{current_pair}\t{sum_count}")
    if sum_count == 1:
        yield current_n



# ### Generator testing
# init_n = 6
# init_list = [1, 2, 3, 4,]
# [i for i in sequence_gen(init_n, init_list)]

def ulam_sequence(n_digits: int) -> list:
    tmp: list
    n: int = 0
    ulam_digits: list = list()
    while n < n_digits:
        n += 1
        if n < 3:
            ulam_digits.append(n)
        else:
            tmp = [i for i in sequence_gen(n, ulam_digits)]
            if len(tmp) == 1:
                ulam_digits.append(n)
    return ulam_digits

ulam_sequence(10)
ulam_sequence(100)
ulam_sequence(340)


# def ulam_sequence(n_digits: int):
#     max_n = float(n_digits)
#     n: float = 0.
#     while n <= max_n:
#         n += 1.
#         if n < 3.:
#             print(n)
#             ulams.append(n)
#         else:
#             ulam_generator

#             sum_count = 0.
#             for i in ulams:
#                 for j in ulams:
#                     if i < j:
#                         current_pair = sorted((j, i))
#                         if sum(current_pair) == n:
#                             sum_count += 1.
#             if sum_count == 1.:
#                 print(n)
#                 ulams.append(n)









#############################################################
### Function with working algo.
# def ulam_sequence(n_digits: int):
#     sum_count: float # Aggregate count of sum of ulam numbers
#     current_pair: tuple
#     n_digits: float = 10.
#     n: float = 0.
#     ulams: list = [] # Keep a list of approved numbers
    
#     while n <= n_digits:
#         n += 1.
#         if n < 3.:
#             print(n)
#             ulams.append(n)
#         else:
#             sum_count = 0.
#             for i in ulams:
#                 for j in ulams:
#                     if i < j:
#                         current_pair = sorted((j, i))
#                         if sum(current_pair) == n:
#                             sum_count += 1.
#             if sum_count == 1.:
#                 print(n)
#                 ulams.append(n)
