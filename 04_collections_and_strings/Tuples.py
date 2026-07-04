
# tuple is not changeable
tup = (1,32, 45, 65, 12, 55 ) # if you make a single value tuple then comma is necessary
print(type(tup), tup)

# same as list functionalities
# lst = (i for i in range(4)) # this is not tuple
# print(lst)

if 32 in tup:
    print("Yes 32 in tuple.")