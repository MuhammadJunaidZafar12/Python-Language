# import os
# os.system("python --version")
x = int(input("Enter the value of x: "))
# x is a variable to match
match x:
    # if x is 0
    case 0:
        print("x is 0")
    case 4:
        print("Case is 4")

    case _ if x!=90 :
        print(x, "is not 90")
    case _ if x != 80:
        print(x, "is not 80")
    case _: # default case show by underscore
        print(x)
