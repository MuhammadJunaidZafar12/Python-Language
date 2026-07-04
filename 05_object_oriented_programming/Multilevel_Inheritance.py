class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show(self):
        print(f"The name is {self.name}")
        print(f"The species is {self.species}")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species = "dog")
        self.breed = breed

    def show(self):
        Animal.show(self)
        print(f"The breed is {self.breed}")


class GoldenRetriever(Dog):
    def __init__(self, name, color):
        # super().__init__(name)
        # self.name = name
        Dog.__init__(self, name, breed = "Golden Retriever")
        self.color = color

    def show(self):
        Dog.show(self)
        print(f"Color {self.color}")

o = GoldenRetriever("Dog", "Black")
o.show()