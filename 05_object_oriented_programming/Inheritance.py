class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show(self):
        print(f"The name of Employee: {self.id} and {self.name}")

class Programmer(Employee):
    def showlanguage(self):
        print("The default language is python")

e = Employee("Faziii", 420)
e.show()
e2 = Programmer("Waris", 2)
e2.show()
e2.showlanguage()


