'''
The Constructor: Setting Things Up (__init__)
The __init__ method is special. It's called the constructor. It's automatically run whenever you create a new object from a class.

What's it for? The constructor's job is to initialize the object's attributes - to give them their starting values. It sets up the initial state of the object.

'''

# The Constructor: Setting Things Up (__init__)
# (__init__) likh karke constructor ko initiate kar sakte hai


class employee:

    def __init__(self, salary, name, bond): # __init__ is a by defoult meaning constructor, it use to initializ an ombject
        self.salary = salary # create an instance attribute of name salary and assing it with salary 
        self.name = name
        self.bond = bond
        # this was consteructor in action
        
    def get_salary(self):# self is important here self is a way to reference the object of a class which is being created
        return self.salary
        # pass # we use pass when we don't whant to anything currently, we'll write the code letter 
    def get_info(self):
        print(f"The name of the employee is {self.name}. salary is {self.salary}. and the bond is for{self.bond} years")
    # this was methord in action 

e1 = employee(34000, "john doe", 4)
# print(e1.get_salary())    
e1.get_info()

