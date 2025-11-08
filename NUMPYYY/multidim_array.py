import numpy as np
arr=np.array([['A','B','C'],
            ['D','E','F'],
            ['G','H','I']])
print(arr.ndim)
print(arr.shape)
print(arr.size)
# multidim indexing faster than chain indexing
print(arr[1,1])
