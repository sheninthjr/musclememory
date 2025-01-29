
class Animal:
    def sound(self):
        return f"The animal sounds weird"
    
class Dog(Animal):
    def sound(self):
        return f"Dog Barks"
    
class Cat(Animal):
    def sound(self):
        return f"Cat meows"
    
def make_sound(animal):
    print(animal.sound())

dog = Dog()
make_sound(dog)