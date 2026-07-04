# default arguments

# def average(a=5, b=8):
#     print("Average is: ", (a+b)/2)

# average(b=6,a=4)

# keyword arguments
# mean we first write the value of b and then write the value of a then no problem occurs python detects automatically in arguments

# required argument
# we must give this argument

# variable length argument as tuple

def average(*numbers):
    print(type(numbers))  #take the numbers as tuple
    summ = 0
    for i in numbers:
        summ = summ + i
    return summ / len(numbers) # we also return the values in functions

c = average(5, 6, 7, 1)
print("The average is: ", c)

# argument as dictionary will discuss in dictionary topic
# def name(**names):
#     print(type(names))
#     print("Hello", names["fname"], names["mname"],"and", names["lname"])
#
# name(mname="Junaid", lname = "Ali", fname="Hassan")