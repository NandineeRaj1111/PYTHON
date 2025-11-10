import numpy as np
# scalar arithmetic
arr=np.array([1,2,3])
arr2=np.array([2.34,5.67,8.99])
print(arr+1)
print(arr**2)
print(np.sqrt(arr))
print(np.round(arr2))
print(np.pi)

# vectorised math function
radii=np.array([2,4,8])
print("area is :")
print(np.pi*radii**2)
# element wise arithmetic
a = np.array([3,5,7])
b= np.array([4,6,9])
print(a+b)
print(a-b)
print(a**b)

# filtering
# comparison op
marks=np.array([98,87,67,56,44])
marks[marks<60]=0 # means they wont get grading i.e they are fail
print(marks)