# 1. Decorators in Python
# Q.1 - Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints "Hello!"

# def logger(func):
#     def wrapper():
#         print("Function is being called !")
#         func()
#     return wrapper

# @logger
# def say_hello():
#     print("Hello")

# say_hello()


# Q.1.2 - Write a decorator timer that calculates how long a function takes to execute. Test it with a function that sums numbers from 1 to 1,000,000.

# from time import time 
# def timer(func):
#     def wrapper(n):
#         t1 = time()
#         result = func(n) # adding a result variable to get valur of sum, not just time
#         t2 = time()
#         print(t2-t1)
#         return result
#     return wrapper

# @timer
# def sum_1m(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum += i
#     return sum

# a = sum_1m(100000)
# print(a)

# 2 - Getters and Setters
# Q 2.1- Create a class Employee with a private attribute _salary.
# Use @property to define a getter for salary.
# Use @salary.setter to prevent setting negative values (print a warning instead).
# Create an object and test by setting positive and negative salaries.

# class Employee:
#     def __init__(self, salary): # priavte attribute
#         self._salary = salary

# #  Used @property to define a getter for salary.
#     @property
#     def salary(self):
#         return self._salary

# #  Used @salary.setter to prevent setting negative values (print a warning instead).
#     @salary.setter
#     def salary(self, value):
#         if(value<0):
#             print("Hey please dont set a negative value for salary")
#         else:
#             self._salary = value

# e = Employee(3)
# # e.salary = -765 # trying to print negative salary,  it eill through an error
# e.salary = 55 #trying to print possitive salary
# print(e.salary) # we can not run this without getter which is "property"

# 3 - Static & Class Methods

# Q 3.1 - Create a class MathUtils with:
# A @staticmethod called add(a, b) that returns a + b.
# A @classmethod called description(cls) that prints "This is a utility class for math operations."

# class Mathutiles:
#     def __init__(self):
#         pass

#     @staticmethod
#     def add(a, b):
#         return a + b

#     @classmethod
#     def description(cls):
#         print("This is a utility class for math operations.")

# # this is by creating an object
# # a = Mathutiles
# # print(a.add(3, 4))
# # a.description() # we are not using print coz we can use it directly since it is not returning any thing

# # this is without creating an object
# Mathutiles.description()
# print(Mathutiles.add(4, 6))


# 4 - Magic/Dunder Methods

# 4.1 - Create a class Book with attributes title and author.
# Implement __str__() so that printing the object displays "Title by Author".
# Implement __len__() so that len(book) returns the length of the title.

# class Book:
#     def __init__(self, title, author):
#         self.title = title # attribute
#         self.author = author # attribute

#     def __str__(self):
#         return(f"{self.title} by {self.author}")

#     def __len__(self):
#         return len(self.title)

# b = Book("Python in one hour", "sonu") # this is a title 
# print(b)
# print(len(b)) 
# # in O/P it will also print numbers of charactor in title

# b2 = Book("Java in one hour", "sonu") # this is a title 
# print(b2)
# print(len(b2)) 
# # i can also use b again while printing the difrednt name


# 5 - Exception Handling and Custom Errors
# Q. 5.1 - Write a program that asks the user to enter a number and handles:
# ValueError if the input is not a number
# ZeroDivisionError if you try to divide by zero
# Create a custom exception NegativeNumberError and raise it when the user enters a negative number.

# class NegativeNumberError(Exception):
#     pass

# try:
#     num = int(input("Enter a number "))

#     if num<0:
#         raise NegativeNumberError("Number can not be negative")

#     result = 45/num
#     print(f"The result is {result}")

# except ValueError:
#     print("Error: please enter a proper number")

# except ZeroDivisionError:
#     print("Erro: can not divided by 0")

# except NegativeNumberError as e:
#     print(f"Error: {e}")

# 6 -  map(), filter(), and reduce()
# Q. 6.1 - Use map() to convert [1, 2, 3, 4, 5] into their cubes.
# Use filter() to get only even numbers from [10, 11, 12, 13, 14].
# Use reduce() from functools to find the product of all elements in [1, 2, 3, 4].

# numbers = [1, 2, 3, 4, 5]

# def square(x):
#    return x * x * x
# new = list(map(square, numbers))
# print(new)

# or the diffret approch

# l = [1, 2, 3, 4, 5]

# cube = lambda x: x*x*x
# l1 = list(map(cube, l))
# print(l1)

# filter()

# l = [10, 11, 12, 13, 14]

# f = lambda x: x%2 ==0
# l1 = list(filter(f, l))
# print(l1)

# reduce()
# from functools import reduce

# l = [1, 2, 3, 4]
# product = lambda a, b: a*b
# print(reduce(product, l))

# 7 - Walrus Operator
# Q.7.1 - Use the walrus operator to read input until the user enters "quit". Print each input as it is entered.

# while(text := input("Enter somthing: ")) != "q":
#     print(f"You entered {text}")

# Q.7.2 - Use the walrus operator in a list comprehension to store lengths of words from ["python", "rocks", "ai"] in a list while filtering out words shorter than 4 characters

# words = ["python", "rocks", "ai"]

# lengths = [n for w in words if (n := len(w))>= 4]

# print(lengths)

#  8 - *args and **kwargs
# Q. 8.1 - Write a function sum_all(*args) that accepts any number of integers and returns their sum.

# def sum_all(*args):
#     sum = 0
#     for item in args:
#         sum += item
#     return sum
# print(sum_all(3, 4, 5))

# Q. 8.2 - Write a function print_details(**kwargs) that prints key-value pairs passed as arguments, for example:
# def  print_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_details(name="Alice", age=25, city="Delhi")   


# 9 - Bonus Challenges
# 9.1 - Combine a decorator with *args and **kwargs support so it can wrap any function regardless of its parameters.
# 9.2 - Implement __add__ in a Vector class so that adding two Vector objects returns a new Vector with summed components.
# 9.3 - Create a small program where invalid user input raises a custom exception, logs the error, and continues execution instead of crashing
