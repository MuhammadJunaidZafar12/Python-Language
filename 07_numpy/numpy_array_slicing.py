import numpy as np
# example # 01
array1 = np.array([10, 20, 30, 40, 50, 60, 70])
print(array1[1:3]) # [20,30]
print(array1[1:8:2]) # [20, 40, 60] # indexing not gives error if out of bound
print(array1[-1:-3:-1]) # [70, 60]
print(array1[::2]) # [10, 30, 50, 70]
# print the reverse array
print(array1[::-1]) # [70, 60, 50, 40, 30, 20, 10]

# example # 02
array1 = np.array([[15, 16, 17],
                   [25, 26, 27],
                   [35, 36, 37],
                   [45, 46, 47]])

print(array1[1, ]) # 25, 26, 27
print(array1[:, 1]) # 16, 26, 36, 46
print(array1[1:3, 1:3]) # 26 27
                        # 36 37
print(array1[1:3, ]) # [25, 26, 27],
                     # [35, 36, 37]
print(array1[:, 1:3])# [16, 17],
                     # [26, 27],
                     # [36, 37],
                     # [46, 47]])
print(array1[1:3, 1]) # 26, 36
print(array1[1:3, :1]) # 25, 35
print(array1[1:3, 1:]) # 26, 27
                       # 36, 37

