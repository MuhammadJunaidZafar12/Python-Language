# ******************** Employee Class **************************
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromstr(cls, string_):
        return cls(string_.split("-")[0], int(string_.split("-")[1]))

# ********************** main *************************************

e1 = Employee("Junaid", 12000)
print(e1.salary)
print(e1.name)

string = "Ali-12000"
e2 = Employee.fromstr(string)
print(e2.salary)
print(e2.name)
