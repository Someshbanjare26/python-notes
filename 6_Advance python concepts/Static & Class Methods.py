class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    # this is an instance methord(default)
    def print_info(self):  # it is a static methord
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    # static methord(it  doesn't need/requir self)
    @staticmethod 
    def sum(a, b): # yaha sum(self, a, b) hota lekin hame self use hi nahi akrna hai, kyoki fir e2.sum me e2 self ka refrence hoga and e2 is a heavy object hamko vo nai chahiye, we just want to perform simple calculation under the instence class
        return a+b

    # class methods
    @classmethod # this is a decorator
    def print_company(cls):#cls is nothing but just a class method
        print(cls.company)
    # now we want to cahnege the company
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
        
e1 = Employee("jack", 34555)
e2 = Employee("jill", 34665)
# print(Employee.company)
# print(Employee.name) ---> this will throw an error becouse don't have name as a class variable ok 

# e1.print_info()
# e2.print_info()
# print(e2.sum(5, 23))
e1.print_company()
e1.change_company("Acer")
e1.print_company()

