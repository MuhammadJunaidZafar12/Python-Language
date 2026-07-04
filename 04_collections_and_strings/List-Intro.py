# List is order collection of data items

l = [3, 6, 8, "Junaid", True, 6, 8, 9, 10]
# print(l)
# print(l[0])
# print(l[1])
# print(l[2])

# print(l[-3]) # Negative index
# print(l[len(l)-3]) # positive index
# print(l[5-3]) # positive index
# print(l[2])
# number = int(input("Enter the value to check it is in list or not: "))
# if number in l:
#     print("Yes")
# else:
#     print("No")

# if "Jun" in "Junaid":
#     print("Yes")

# print(l)
# print(l[1:8])
# print(l[  1  :  8  :  3  ])
#      start : end : jump

# list comprehension
lst = [i for i in range(4)]
print(lst)
# we also write the if statement in list
lst = [i for i in range(4)  if i%2==0]
print(lst)

# example 2
names = ["milo", "Sarah", "Junaid", "Ali", "Hassan"]
nameswith_O = [item for item in names if 'o' in item]
print(nameswith_O)

# example 3
name2 = ["milo", "Sarah", "Junaid", "Ali", "Hassan"]
nameswith_4 = [item for item in name2 if (len(item)>4)]
print(nameswith_4)