class Employee:
    company = "Apple" #class variable (private)

    def show(self):
        print(f"The name of the employee is {self.name} and the company name is {self.company} ")
    # if we want to change the value of class variable then we write before the function @classmethod
    @classmethod #when we make method without @classmethod then the first argument take as instance if write then take as a class
    def changecompany(cls, newcompany):
        cls.company = newcompany # if we not write the class method before this method then this will make the instance variable and store
                                   # the data in that variable not change the class variable or original variable

emp1 = Employee()
emp1.name = "Junaid"
emp1.show()
emp1.changecompany("Tesla")
emp1.show()
print(Employee.company)