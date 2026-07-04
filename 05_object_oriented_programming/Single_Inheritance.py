class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by the animal!!")

class Dog(Animal):
    def __init__(self, name1, breed):
        Animal.__init__(self, name1, species = "dog")
        self.breed = breed
    def make_sound(self):
        print("Bark")

dog = Dog("Dog", "Dodgy")
dog.make_sound()

animal = Animal("Dog", "Dog")
animal.make_sound()

