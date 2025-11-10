import numpy as np
arr=np.array([[1,2,3,4],
             [76,87,56,43]])
print(np.sum(arr))
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(np.var(arr))
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr)) #gives pos of min element
print(np.sum(arr, axis=0)) #col wise each element sum
print(np.sum(arr, axis=1)) #sum of elements of each row
