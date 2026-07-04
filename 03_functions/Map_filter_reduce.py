# MAP
# def cube(x):
#     return x*x*x
# print(cube(2))
l = [1, 2, 4, 6, 4, 3]
# newl = []
# for item in l:
#     newl.append(cube(item))

# newl = list(map(lambda y : y * y * y, l)) #we use direct lambda function instead of using function name as argument we use direct function in argument
# print(newl)

# def myfunc(a, b):
#   return a + b
#
# x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
# print(list(x))

# FILTER
# def filter_function(a):
#     return a > 2
# newnewl = list(filter(filter_function, l))
# print(newnewl)

# REDUCE

from functools import reduce
# list of numbers
numbers = [1, 2, 4, 6]
#calculate the sum of the numbers
summission = reduce(lambda x, y: x + y, numbers)
print(summission)