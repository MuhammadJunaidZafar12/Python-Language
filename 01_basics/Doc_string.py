def square(n): #doc string is defined just after this def line
    # doc string
    # print(n) #doc string remove due to this print statement if we right doc string then we need to write in the top of function
    '''Takes a number n, returns the square of n'''
    print(n**2)
square(5)
# printing doc string
print(square.__doc__)
