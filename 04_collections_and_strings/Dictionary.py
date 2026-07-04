dic = {
    "Junaid" : "Human Being",
    "Spoon" : "Object"
}

# print(dic["Junaid"])
#
info = {'name' : 'junaid','age': 20, "eligible" : True}
# print(info['name']) #if name key not found then gives error
# print(info.get('name')) #if name key not found then gives (none)
#
# # Displaying the keys
#
# print(info.keys())
# print(info.values())
# # using for loop
# for key in info.keys():
#     print(f"The value corresponding to the {key} is {info[key]}")

# Iterate over keys
for key in info:
    print(f"{key} ")
# Iterate over values
for value in info.values():
    print(f"{value} ")
# Iterate over key-value pairs
for key,value in info.items():
    print(f"{key}:{value}")

# using items method
print(info.items()) #  gives us key value pairs

#using for loop
# for key, value in info.items():
#     print(f"The value corresponding to the {key} is {value}")


# nested dictionary

d = {1: 'Geeks', 2: 'For',
        3: {'A': 'Welcome', 'B': 'To', 'C': 'Geeks'}}

print(d)

d[3] = {"B":"Good Bye", "C":"Good Night"}
print(d)