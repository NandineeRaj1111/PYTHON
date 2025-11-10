# broadcasting allows numpy to perform op on arrays ,
# with diff shapes by virtually expanding dimensions,
# so they match larger arrays shape
# dim have same size or one of the dim is 1
import numpy as np
a= np.array([[1,2,3,4]])
b=np.array([[1],[2],[3],[4],[5]])
# b= np.array([[1,2],[2,4],[3,5],[4,9]]) here comes broadcast error
print(a.shape)
print(b.shape)
print(a*b)