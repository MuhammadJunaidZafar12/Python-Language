# recursion is the process of finding something in terms of itself
# finding the factorial of any number

def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number * factorial(number-1)

n = int(input("Enter the number for finding factorial: "))
print(factorial(n))

