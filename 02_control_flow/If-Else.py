# if else statement

a = int(input("Enter Your Age: "))
# print("Your Age Is: ", a)
# Condition operator
# <, >, <=, >=, ==, !=
if a>90:
    if 90 < a < 100:
        print("Age is between 90-100")
    print("You are over age you can derive")
elif a>18:
    print("You are ", a , "Years old, you can derive")
else:
    print("You cannot drive")

# nested if else
#  in if_else