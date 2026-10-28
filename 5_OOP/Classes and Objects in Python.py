# Classes and Objects: The Blueprint and the Building

# Class: Think of a class as a blueprint or a template. It defines what an object will be like – what data it will hold and what actions it can perform. It doesn't create the object itself, just the instructions for creating it. It's like an architectural plan for a house.
# Object (Instance): An object is a specific instance created from the class blueprint. If "Car" is the class, then your red Honda Civic is an object (an instance) of the "Car" class. Each object has its own unique set of data. It's like the actual house built from the architectural plan.

# class --> template
# object --> specific instance created by the the template

class employee:
    company = "Hp"

    def get_salary(self): # self is a way to refrence of the class which is being created
        # print(self)
        return 34000

e = employee() # An class of an Employee is created here
print(e.get_salary()) # Employee get salary methord is called

e2 = employee()
print(e2.get_salary())









