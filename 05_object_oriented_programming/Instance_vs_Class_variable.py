class Employee:
    __company = "Apple" #class variable (private)
    noofemployes = 0
    def __init__(self, name):
        self.name = name         # instance variable
        self.raise_amount = 0.02
        Employee.noofemployes += 1


    def show(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.noofemployes} sized {self.__company} is {self.raise_amount}")

emp1 = Employee("Junaid")
emp1.show()
# Employee.show(emp1)
emp2 = Employee("Ali")
emp2.show()
