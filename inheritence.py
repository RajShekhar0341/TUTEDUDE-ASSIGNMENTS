# Base class (Parent)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animals make sounds")


# Derived class (Child)
class Dog(Animal):
    def speak(self):
        print(self.name, "says Woof Woof!")


# Another Derived class
class Cat(Animal):
    def speak(self):
        print(self.name, "says Meow!")


# Main program
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()
cat.speak()