# Magic/Dunder Methods ---> below this are thew dunder methods 
class Employee:
    company = "HP"
    def __int__(self, name, salary):
        self.name  = name
        self.salary = salary
    def __str__(self): #this is Dunder methods
        return f"The name is {self.name} and the salary is {self. salary}"

    def __repr__(self): # this mostly used by devloper for debuge
        return f" name:  {self.name} \n salary: {self. salary}"

    def __len__(self):
        return len(self.name)

e = Employee("Sonu", 8945676)
print(len(e)) # this will print the lenth of the string which is name here
# print(e.name, e.salary)
# print(str(e)) # str is basicaly for user
# print(repr(e)) #repr is basicaly for devlopers who try to debug