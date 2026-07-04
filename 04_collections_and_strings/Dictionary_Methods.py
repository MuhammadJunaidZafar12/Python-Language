ep1 = {
    122 : 45,
    123 : 89,
    567 : 69,
    670 : 69

}

ep2 = {
    222 : 45,
    223 : 89
}
# one remove key value pair
# ep1.pop(122)
# print(ep1)
key,value = ep1.popitem() # remove last key value pair in dictionary
print(f" deleting the {key} and {value}")
# ep1.update(ep2)
# ep1.clear()
print(ep1)

# empty dictionary
empt = {}
print(empt)

# we also delete the dictionary using del keyword
# del empt # del the entire dictionary
del ep2[222]  # del the key which in dictionary and its value which given
print(ep2)

# making dictionary with dict constructor

d = dict(number = 15, b = 16)
print(type(d))
print(d)

# adding new key and value in dictionary
d["age"] = 20
print(d)

# updating an existing value
d["number"] = 45
print(d)