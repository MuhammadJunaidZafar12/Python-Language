class Employee:
    name = "junaid"
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    def __str__(self):
        return f"The name of the employee is {self.name}"
    def __repr__(self):
        return f"The name of the employee is {self.name} repr"
    def __call__(self):
        print("I am good")

e = Employee()
print(e.name)
print(e) #this show data of __str__ method which string is returning
print(len(e))
print(str(e))
print(repr(e))
e() # call methods data show here