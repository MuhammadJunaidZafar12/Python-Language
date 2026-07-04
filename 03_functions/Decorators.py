# python decorators are a powerful and versatile tool that allow you to modify the behaviour of functions and methods
# syntax of arguments in decorator
#         def decorator_name(func):
#             def wrapper(*args, **kwargs):
#                 # Add functionality before the original function call
#                 result = func(*args, **kwargs)
#                 # Add functionality after the original function call
#                 return result
#             return wrapper
#
#
#         @decorator_name
#         def function_to_decorate():
#             # Original function code
#             pass

#***********************************************************#
# example of arguments
# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Good Morning")
#         fx(*args, **kwargs)
#         print("Thanks for using this function")
#     return mfx

# def hello():
#     print("Hello World")
# greet(hello)()
# @greet
# def add (a, b):
#     print(a+b)
# add(3, 9)
# greet(add)(3,6)

# example 2
def decorator(func):

    def wrapper():
        print("Before calling")
        func()
        print("After calling")
    return wrapper
# applying decorator
@decorator
def greet():
    print("Hello world")

greet()


# passing function as argument
# Assigning a function to a variable
def greet(n):
    return f"Hello, {n}!"

say_hi = greet  # Assign the greet function to say_hi
print(say_hi("Alice"))  # Output: Hello, Alice!

# Passing a function as an argument
def apply(f, v):
    return f(v)

res = apply(say_hi, "Bob")
print(res)  # Output: Hello, Bob!

# Returning a function from another function
def make_mult(f):
    def mult(x):
        return x * f
    return mult

dbl = make_mult(2)
print(dbl(5))  # Output: 10