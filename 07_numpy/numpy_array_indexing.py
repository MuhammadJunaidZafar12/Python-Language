import numpy as np

array1 = np.array([10, 20, 30, 40, 50])
print(array1[0])
print(array1[-1])

list1 = [[10, 20, 30],
         [40, 50, 60],
         [70, 80, 90]]
array1 = np.array(list1)
print(array1[1,2])
print(array1[0,])
print(array1[:, 1])

# by default row major order

#column major order
# order='F', Fortran-style, column-major (fill down columns first)
B = np.arange(1, 7).reshape((2, 3), order='F')
print(B)

