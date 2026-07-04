class Person:
    name = "Junaid"
    age = "20"
    occupation = "Software Developer"
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a = Person()
b = Person()
b.name = "Ali"
b.age = "23"
# print(a.name)
# print(a.age)
a.info()
b.info()
