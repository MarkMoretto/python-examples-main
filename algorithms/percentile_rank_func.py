"""
Percentile rank

Params:
    iterable: list, array, etc., of numeric values
    percentile: the percentile to find. Should be integer data type. (e.g. - 25 = 25th, 96 = 96th)

Ref: https://www.wallstreetmojo.com/percentile-rank-formula/
"""


def percent_rank(iterable, percentile):
    it = sorted(iterable, reverse=False)
    ddict = {k:v for k, v in enumerate(it, start=1)}
    
    n = len(it)
    rank = (percentile/100) * (n + 1)

    r_n, r_r = divmod(rank, 1)
    
    for k in range(1, n):
        x, y = 0, 0
        if rank == k:
            x, y = ddict[k], ddict[k]
        elif rank > k and rank < k + 1:
            x, y = ddict[k], ddict[k + 1]
        xy_sum = x + y
        if xy_sum > 0:
            print((y - x) * r_r + x)
            break


### Tests
p = 25
test_data_1 = [122, 112, 114, 17, 118, 116, 111, 115, 112]
assert (percent_rank(test_data_1, p) == 111.5), "Error: Test 1"


p = 75
test_data_2 = [1155, 1169, 1188, 1150, 1177, 1145, 1140, 1190, 1175, 1156]
assert (percent_rank(test_data_2, p) == 1179.75), "Error: Test 2"


p = 96
test_data_3 = [435.0, 435.0, 442.0, 44.0, 445.0, 454.0, 456.0, 456.0, 456.78, 459.0, 461.0,
        465.0, 468.0, 469.0, 471.0, 471.0, 472.0, 472.0, 477.0, 477.0, 477.0, 477.0,
        481.0, 488.0, 489.0]
assert (percent_rank(test_data_3, p) == 488.96), "Error: Test 3"
