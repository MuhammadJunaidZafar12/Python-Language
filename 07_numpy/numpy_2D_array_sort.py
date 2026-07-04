import numpy as np

# by default sort in ascending order
# this also generates the copy not change the original array
# this sort according to x_axis by default but you want to write the axis then write the axis = 1
x = np.array([[12, 11, 15],
              [21, 25, 20],
              [18, 27, 16]])
y = np.sort(x, axis=1) # axis = 0 --> row wise
print(y)

# if we want to print in descending order
# this also generates the copy not change the original array
# if we want to sort in y_axis
x = np.array([[12, 11, 15],
              [21, 25, 20],
              [18, 27, 16]])
y = np.sort(x, axis=0) # axis = 0 --> column wise
print(y)

# np.argsort() --> this gives the sorted arrays indexes
# this also generates the copy not change the original array
x = np.array([[12, 11, 15],
              [21, 25, 20],
              [18, 27, 16]])
y = np.argsort(x)
print(y)

# sort()
# this change the original array
x = np.array([[12, 11, 15],
              [21, 25, 20],
              [18, 27, 16]])
x.sort()
print(x)