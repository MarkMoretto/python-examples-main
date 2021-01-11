
"""
Purpose: Stakoverflow question finding first and last coordinates for values in matrix
Date created: 2019-12-28

URI: https://stackoverflow.com/questions/59511521/how-to-get-start-and-end-of-subsection-of-2d-array-where-a-condition-holds/59511652#59511652

Contributor(s):
    Mark M.
"""


a = [[0, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]]


results_list= list()
while True:
    for i, v in enumerate(a):
        if 1 in v:
            results_list.append([i, v.index(1)])
    first_pair = results_list[0]
    last_pair = results_list[-1]
    break



results_list[0]

results_list[-1]