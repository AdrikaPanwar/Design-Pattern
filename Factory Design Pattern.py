# PROBLEM

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")


def client_code(animal_type: str):
    factory = AnimalFactory()
    animal = factory.create_animal(animal_type)
    print(f"The animal says: {animal.speak()}")


client_code('dog')
client_code('cat')
