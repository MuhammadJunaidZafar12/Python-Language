class Employee:
    def __init__(self):
        self.__name = "Junaid"

a = Employee()
# print(a.__name) # double underscore indicates that the attribute is private and not accessible by default public
print(a._Employee__name)  # we access private attribute using this method or technique

# print(a.__dir__())

# Protected attributes and functions are accessible