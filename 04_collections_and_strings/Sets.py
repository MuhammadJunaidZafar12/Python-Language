# Sets
# The main point, values not repeated
# sets are unordered collections of data type
# and other like lists
# are separated with comma and enclosed in curly braces
# and indexes value are unchangeable
# order of output is not gurenteed
s = {2, 4, 6, 2}
print(s)

s.add(7)

for value in s:
    print(value)

# junaid = {} # this is type dictionary
junaid = set() # this is type set
print(type(junaid))