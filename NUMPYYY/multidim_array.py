import numpy as np
arr=np.array([['A','B','C'],
            ['D','E','F'],
            ['G','H','I']])
print(arr.ndim)
print(arr.shape)
print(arr.size)
# multidim indexing faster than chain indexing
print(arr[1,1])
word=arr[0,1]+arr[0,0]+arr[1,0]
wordd=arr[1,0]+arr[0,0]+arr[1,0]
print(f"if you are {word}, then I am your {wordd}")

