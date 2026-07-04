
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}

print(s1.union(s2))
s1.update(s2) # change the set s1 with update method
print(s1, s2)

# intersection
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}

s1.intersection_update(s2)
print(s1)

# symmetric difference
# items which are not same
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}

s1.symmetric_difference_update(s2)
print(s1)

# s1 - s2 in sets
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}

s1.difference_update(s2)
print(s1)

# disjoint set --> which have no common elements
print(s1.isdisjoint(s2))

s1 = {1,2,3,4,5}
s2 = {2,3}
# super set and sub set
print(s1.issuperset(s2))
print(s2.issubset(s1))

# removing item from the list
# s1.remove(5) # if number not found then gives error
s1.discard(1) # if number not found then not gives error
print(s1)

item = s1.pop() # remove any number from the set because the number are unordered in set
print(item)
print(s1)

# we also del the entire set
# del s1

# if we want to clear all the items in the set
s1.clear()
print(s1)

info = {"carla", 19, False, 5.9}

if "carla" in info:
    print("carla is in info")
else:
    print("carla is not in info")