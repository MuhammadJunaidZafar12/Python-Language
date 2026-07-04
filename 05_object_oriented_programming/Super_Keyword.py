class ParentClass:
    def parent_method(self):
        print("This is parent method!!")

class ChildClass(ParentClass):
    # def parent_method(self):
    #     print("Junaid")
    #     super().parent_method()

    def child_method(self):
        print("This is child method!!")
        super().parent_method()
child_obj = ChildClass()
child_obj.child_method()
child_obj.parent_method()

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang

obj1 = Programmer("Junaid", 412, "Python")
print(obj1.name)
print(obj1.id)

