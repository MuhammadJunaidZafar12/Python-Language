# Constructor
# it calls every time when we make an object and it also runs automatically
class Person:
    # making a constructor
    # default constructor
    # def __init__(self):
    #     print("Hello World")
    # argument constructor
    def __init__(self, n, o):
        print("Hay I am a developer")
        self.name = n
        self.occ = o

    # name = "Junaid"
    # occupation = "Developer"
    def info(self):
        print(f"{self.name} is a {self.occ}")

c = Person()
a = Person("Junaid", "Developer")
b = Person("Adnan", "HR")
a.info()
b.info()