import numpy as np
# Arithmetic operations
# addition and subtraction and multiplication is also as addition

x = np.array([[1, 2],
              [3, 4]])

y = np.array([[11, 12],
              [13, 14]])

z = x + y
print(z)

#matrix multiplication
x = np.array([[1, 2],
              [3, 4]])

y = np.array([[11, 12],
              [13, 14]])

z = x @ y
print(z)

#division
x = np.array([[1, 2],
              [3, 4]])

y = np.array([[11, 12],
              [13, 14]])

z = y / x
print(z)

#floor division --> this skips the decimal value only pick the before the decimal value
x = np.array([[1, 2],
              [3, 4]])

y = np.array([[11, 12],
              [13, 14]])

z = y // x
print(z)

# exponentiation
x = np.array([[1, 2],
              [3, 4]])

y = np.array([[11, 12],
              [13, 14]])

z = y ** x
print(z)

# reminder
x = np.array([[1, 2],
              [3, 4]])

y = np.array([[11, 12],
              [13, 14]])

z = y % x
print(z)

# transpose
x = np.array([[1, 2],
              [3, 4]])

y = np.array([[11, 12],
              [13, 14]])


print(x.transpose())