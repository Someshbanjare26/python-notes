'''

Class vs. Instance Attributes:
Class Attributes: These are shared by all objects of the class. Like species in our Dog class. All dogs belong to the same species. They are defined outside of any method, directly within the class.

Instance Attributes: These are specific to each individual object. name and breed are instance attributes. Each dog has its own name and breed. They are usually defined within the __init__ method.

'''


class employee:
    company = "Asus" #this is a class atribute 

    def __init__(self, salary, name, bond, company ): # __init__ is a by defoult meaning constructor, it use to initializ an ombject
        self.salary = salary # create an instance attribute of name salary and assing it with salary 
        self.name = name
        self.bond = bond
        self.company = company
        # this was consteructor in action
        
    def get_salary(self):# self is important here selfe is a way to reference the object of a class which is being created
        return self.salary
        # pass # we use pass ehrn we don't whant to anything currently, we'll write the code letter 
    def get_info(self):
        print(f"The name of the employee is {self.name}. salary is {self.salary}. and the bond is for{self.bond} years")
    # this was methord in action 

e1 = employee(34000, "john doe", 4, "tesla")
print(e1.company) # it always print instance attribute whenever present, if it is not present in will print class attribute 
# if you want to print class attribute always you can do somthing like this 
print(employee.company) # it will print class attribute, this is printing becouse we use tha class name 

# object introspection
# object introspection is a way to find all the methords that all the prticuler object in python has
print(dir(e1))