l = [11, 12, 9, 1, 2, 4, 6]
print(l)
l.append(9)
l.sort() # sort in ascending order
print(l)
l.sort(reverse=True) # sort in descending order
print(l)
l.reverse() # make our list reverse
print(l)

print(l.index(9)) #This method return the index of the first occurrence of the list item
print(l.count(9)) # how many times 9 in the list

# not do this
# m = l # store the reference of l in m
# m[0] = 0 # here our main list l is also changes
# print(l)

# not change the original list l
m = l.copy()
m[0] = 0
print(l)

l.insert(1, 899)
print(l)

# extends method in list
j = [1000, 1100, 2000]
l.extend(j) # l changes
print(l)

# extends method in list
j = [1000, 1100, 2000]
k = l + j # l not changes
print(l)
print("The value of k is: ", k)

l.sort(reverse=True)
print(l)