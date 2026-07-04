# length of string
names = "Junaid,zaid"
print(len(names))

# example 2
# **************  string slicing  ************************
fruit = "mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
print(fruit[0:4]) #including 0 but not 4
print(fruit[:4]) # python automatically starts with 0 index
print(fruit[1:4])
print(fruit[0:-3]) # this is equal to print(fruit[0:len(fruit)-3])
#
print(fruit[-1:4]) # is equal to print(fruit[len(fruit)-1: len(fruit)-4])

nm = "harry"
print(nm[-4:-2])
