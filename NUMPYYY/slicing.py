import numpy as np
arr=np.array([[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]])
# array[start:end:step]
print(arr[-1])
print(arr[0:3])
print()

print(arr[0:3:2]) 
print(arr[::2])
# these both give the same result

# reversed order
print(arr[::-1])
print()
print(arr[:,0]) #this will select all rows but 1st comlumn
print(arr[:,::2])
# reversing
print(arr[:,::-1])
print(arr[2:,2:])