# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is")
# # try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#     print("invalid input")

# print("some important code")

# example 2
try:
    num = int(input("Enter the number in integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("index Error")