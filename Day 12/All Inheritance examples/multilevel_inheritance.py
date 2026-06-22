class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        return f"{self.name} is breathing."

    def eat(self):
        return f"{self.name} is eating."


class Mammal(Animal):

    def __init__(self, name, fur_color):
        super().__init__(name)            
        self.fur_color = fur_color

    def feed_milk(self):
        return f"{self.name} is a mammal."


class Dog(Mammal):
    def __init__(self, name, fur_color, breed):
        super().__init__(name, fur_color) 
        self.breed = breed

    def bark(self):
        return f"{self.name} says: Woof! Woof!"

    def display_dog_info(self):
        print(f"Name      : {self.name}")
        print(f"Breed     : {self.breed}")
        print(f"Fur Color : {self.fur_color}")


def run_demo():
    dog = Dog(name="Bruno", fur_color="Golden", breed="Labrador")

    print("Output:")
    dog.display_dog_info()
    print(dog.breathe())     
    print(dog.eat())         
    print(dog.feed_milk())  
    print(dog.bark())        
