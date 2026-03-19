# Method Overriding in Python

# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")
    
    def move(self):
        print("Animal moves")


# Child class 1 - overrides speak() method
class Dog(Animal):
    def speak(self):
        print("Dog barks: Woof! Woof!")
    
    def move(self):
        print("Dog runs on four legs")


# Child class 2 - overrides speak() method
class Cat(Animal):
    def speak(self):
        print("Cat meows: Meow! Meow!")


# Child class 3 - uses parent's speak() method
class Bird(Animal):
    def move(self):
        print("Bird flies in the sky")


# Demonstrating method overriding
if __name__ == "__main__":
    # Create objects
    dog = Dog()
    cat = Cat()
    bird = Bird()
    animal = Animal()
    
    # Call methods - overridden methods are executed
    print("=== Method Overriding Demo ===\n")
    
    animal.speak()  # Output: Animal makes a sound
    animal.move()   # Output: Animal moves
    
    print()
    
    dog.speak()     # Output: Dog barks: Woof! Woof! (overridden)
    dog.move()      # Output: Dog runs on four legs (overridden)
    
    print()
    
    cat.speak()     # Output: Cat meows: Meow! Meow! (overridden)
    cat.move()      # Output: Animal moves (inherited)
    
    print()
    
    bird.speak()    # Output: Animal makes a sound (inherited)
    bird.move()     # Output: Bird flies in the sky (overridden)