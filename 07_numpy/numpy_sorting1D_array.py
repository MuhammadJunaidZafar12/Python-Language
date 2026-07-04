import numpy as np

# by default sort in ascending order
# this also generates the copy not change the original array
x = np.array([7, 2, 3, 9, 6])
y = np.sort(x)
print(y)

# if we want to print in descending order
# this also generates the copy not change the original array
x = np.array([7, 2, 3, 9, 6])
y = np.sort(x)[::-1]
print(y)

# np.argsort() --> this gives the sorted arrays indexes
# this also generates the copy not change the original array
x = np.array([7, 2, 3, 9, 6])
y = np.argsort(x)
print(y)

# sort()
# this change the original array
x = np.array([7, 2, 3, 9, 6])
x.sort()
print(x)