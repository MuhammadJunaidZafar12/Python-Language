import numpy as np

list1 = [10, 20, 30, 40, 50]
array1 = np.array(list1)
print(array1)
print(type(array1))
print(array1.dtype)

list1 = [10, "20", True, 40, 50]
array1 = np.array(list1)
print(array1)
print(type(array1))
print(array1.dtype)


# numpy array datatype string
list1 = [10, '20', 30, 40, 50]
array1 = np.array(list1)
print(array1)
print(type(array1))
print(array1.dtype)

# numpy array datatype float
list1 = [10, 20.40, 30, 40, 50]
array1 = np.array(list1)
print(array1)
print(type(array1))
print(array1.dtype)

# we can also change the datatype explicitly
# numpy array datatype float
list1 = [10, 20, 30, 40, 50]
array1 = np.array(list1, dtype=float)
print(array1)
print(type(array1))
print(array1.dtype)

# we can also change the datatype explicitly
# numpy array datatype float
# we use Unicode for char and string like below
list1 = [10, 20, 30, 40, 50]
array1 = np.array(list1, dtype='U32')
print(array1)
print(type(array1))
print(array1.dtype)

#using a range
array1 = np.arange(1, 8)
print(array1)

#using reshape and range
# reshape(2, 3) mean 2 rows and 3 columns
print("Two rows and three column")
array1 = np.arange(11, 17).reshape(2,3)
print(array1)

# reshape(3, 2) mean 3 rows and 2 columns
print("three rows and two column")
array1 = np.arange(11, 17).reshape(3, 2)
print(array1)

# print("If we want to adjust 6 element in 3 by 3 row then this make an error we need to pass exact elements")
print("three rows and three column")
array1 = np.arange(11, 20).reshape(3, 3)
print(array1)

print("4 Number of zeros created in one row ")
# if we want to change the rows and column of zeros
# array1 = np.zeros(4) #to
array1 = np.zeros((4,2))
print(array1)

print("4 Number of ones created in one row")
array1 = np.ones((4,3), dtype = int)
print(array1)


