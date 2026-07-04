# Tuples not change directly but can change indirectly
countries = ("Spain", "italy", "Pakistan", "England", "Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

# we concatenate two tuples directly
countries = ("Spain", "italy", "Pakistan", "England", "Germany")
countries2 = ("Japan", "Australia", "Pakistan")
southeastasia = countries + countries2
print(southeastasia)
print(countries)
print(countries2)

# count function count the occurrence the number in tuple
#index
tuple1 = (0, 1, 2, 3, 3, 31, 1, 13, 3, 3, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
res = tuple1.index(3, 4, 8) # if value not found error occurs
print(res)

