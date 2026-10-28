# 1. Create a Simple Class and Object
# Create a class Car with a method drive() that prints "Car is moving".
# Create an object of Car and call drive().

# class Car: #cass
#     def drive(self): #methord
#         print("Car is moving")
# car1 = Car()# object
# car1.drive()

# 2. Constructor and Attributes
# Create a class Person with a constructor (__init__) that accepts name and age as arguments and stores them as instance attributes.
# Create an object and print the person’s name and age.

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def get_info(self):
#         print(f"The name is {self.name}, and the age is {self.age}")
# p1 = person("sonu", 21)
# p1.get_info()

# 3. Simple Inheritance
# Create a base class Animal with a method sound() that prints "Some sound".
# Create a derived class Dog that overrides sound() to print "Bark!".
# Create an object of Dog and call sound().

class Animal:
    def sound(self):
        print("Some sound")
class Dog():
    def sound(self):
        print("Bark !")

p1 = Dog()
p1.sound()

# Don !




























