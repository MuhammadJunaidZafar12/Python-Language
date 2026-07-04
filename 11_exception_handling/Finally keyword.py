# finally code block is the part of exception handling
def func1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index of the list: "))
        print(l[i])
        return 1
    except:
        print("Some error occur")
        return 0

    finally:
        print("I am always executed")

print(func1())

