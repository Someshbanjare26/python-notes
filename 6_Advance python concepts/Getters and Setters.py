# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def first_name(self):
#          l = self.name.split(" ") # dot split simply returns a list, when we use sapace it strore as list
#         #  print(l)
#          return l[0] # if i do l[1] it will return doe
#     def set_first_name(self, first):
#         l = self.name.split(" ")
#         new_name = f"{first} {l[1]}"
#         self.name = new_name


# e = Employee("jack doe", 34555)
# print(e.first_name())
# e.set_first_name("john")
# print(e.name)

# # e.projects = 6
# # print(e.projects)

# ******** property decorators

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def first_name(self):
             l = self.name.split(" ") # dot split simply returns a list, when we use sapace it strore as list
            #  print(l)
             return l[0]
    
    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name


e = Employee("jack doe", 34555)
print(e.first_name)
e.first_name = "john"
print(e.name)

# note :- To make an attribute read-only define just the @propert decorator(the getter) and leave out the @name.setter methord. tying to set attributr will resukt in an AttributeError

