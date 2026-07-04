import numpy as np

# ***************** dimension ***************************
lists1 = [10, 20, 30, 40, 50]
array1 = np.array(lists1)
print(array1.ndim)  # ndim--> dimension

list1 = [[10,20,30],[40, 50, 60], [70, 80, 90]]
array1 = np.array(list1)
print(array1.ndim)

list1 = [[[10,20,30],[40, 50, 60]],
         [[70, 80, 90], [100, 110, 120]]]
array1 = np.array(list1)
print(array1.ndim)


# ***************** shape ***************************
print("************* shape ****************")
lists1 = [10, 20, 30, 40, 50]
array1 = np.array(lists1)
print(array1.shape)  # shape-->

list1 = [[10, 20, 30],
         [40, 50, 60],
         [70, 80, 90]]
array1 = np.array(list1)
print(array1)
print(array1.shape)

list1 = [[[10,20,30],
          [40, 50, 60]],

         [[70, 80, 90],
          [100, 110, 120]]]
array1 = np.array(list1)
print(array1)
print(array1.shape)

# ***************** size ***************************
lists1 = [10, 20, 30, 40, 50]
array1 = np.array(lists1)
print(array1.size)  # size--> give the size of array

list1 = [[10,20,30],[40, 50, 60], [70, 80, 90]]
array1 = np.array(list1)
print(array1)
print(array1.size)

list1 = [[[10, 20, 30],
          [40, 50, 60]],

         [[70, 80, 90],
          [100, 110, 120]]]
array1 = np.array(list1)
print(array1)
print(array1.size)

# ***************** dtype ***************************
print("dtype")
lists1 = [10, 20, 30, 40, 50]
array1 = np.array(lists1)
print(array1.dtype)  # dtype--> give the datatype of array

list1 = [[10,20,30],[40, 50, 60], [70, 80, 90]]
array1 = np.array(list1)
print(array1)
print(array1.dtype)

list1 = [[[10, 20, 30],
          [40, 50, 60]],

         [[70, 80, 90],
          [100, 110, 120]]]
array1 = np.array(list1)
print(array1)
print(array1.dtype)


# ***************** item size ***************************
print("item size")
lists1 = [10, 20, 30, 40, 50]
array1 = np.array(lists1)
print(array1.itemsize)  # item size--> give the datatype of array element

list1 = [[10,20,30],[40, 50, 60], [70, 80, 90]]
array1 = np.array(list1)
print(array1)
print(array1.itemsize)

list1 = [[[10, 20, 30],
          [40, 50, 60]],

         [[70, 80, 90],
          [100, 110, 120]]]
array1 = np.array(list1)
print(array1)
print(array1.itemsize)