
"""
Purpose: 
Date created: 2020-12-11

https://stackoverflow.com/questions/65261351/calculate-probabilities-of-the-occurrence-of-different-arrays-in-python?noredirect=1#comment115376211_65261351

Contributor(s):
    Mark M.
"""

# import scipy.stats as ss

import numpy as np


array1 = np.array([[2702.703, 2702.703, 500.025],[1060.265, 300.2565, 2702.703],[2702.703, 2702.703, 2702.703]], dtype=np.float32)
array2 = np.array([[1000.235, 2702.703, 500.025],[1060.265, 300.2565, 2702.703],[2702.703, 2702.703, 200.2655]], dtype=np.float32)
array3 = np.array([[2702.703, 1500.326, 500.025],[4520.22, 300.2565, 2702.703],[2702.703, 1245, 2702.703]], dtype=np.float32)

array4 = np.zeros_like(array1)
array5 = np.zeros_like(array1)
array6 = np.zeros_like(array1)

# array5 = array1 + array2 + array3
arrayX = np.array([array1, array2, array3], dtype=np.float32)
arrayY = np.array([array4, array5, array6], dtype=np.float32)

arrayZ = np.dstack((array1, array2, array3))
unique, indices, inverse, counts = np.unique(arrayZ, return_index=True, return_inverse=True, return_counts=True)
freqsZ = dict(zip(unique, counts))

# np.take(array5, [0,9,18])
def softmax(n):
    return max(0, n)

stepsize = arrayX.size // len(arrayX) # 9
rng = np.array(list(range(0, arrayX.size, stepsize))) # 0, 9, 18

array4 = np.zeros_like(array1)
array5 = np.zeros_like(array1)
array6 = np.zeros_like(array1)
for i in range(stepsize):
    tmparrX = np.take(arrayX, rng)
    tmparrY = np.take(arrayY, rng)

    unique, counts = np.unique(tmparrX, return_counts=True)
    freqs = dict(zip(unique, counts))
    tot_values = sum(freqs.values())
    ratios = {k:round(v / tot_values, 6) for k, v in freqs.items()}

    array4[0][0] = ratios[str(array1[0][0])]
    rng += 1

# array4 = np.zeros_like(array1)
# for i in range(len(array5)):
#     for j in range(len(array5[i])):
#         for k in range(len(array5[i][j])):
#             for l in range(len(array5)):
#                 print(i, j, k, array5[i][j][k])



unique, counts = np.unique(array1, return_counts=True)
freq1 = dict(zip(unique, counts))

unique, counts = np.unique(array2, return_counts=True)
freq2 = dict(zip(unique, counts))

unique, counts = np.unique(array3, return_counts=True)
freq3 = dict(zip(unique, counts))



array5 = np.array([array1, array2, array3], dtype=np.float32)


unique, counts = np.unique(array1, return_counts=True)

for el in array

q = (array5 - array5.mean()) / array5.std()



array4 = np.array([[0.03, 0.2, 0.01],[0.22, 0.71, 0.9],[0.15, 0.45, 0.5]],dtype=np.float32)