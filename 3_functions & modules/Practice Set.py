# Q1. Defining a function 
# 1.1 write a function greet() that prints "Hello, python learners!" when called.
# 1.2 write a function square() that returns the squence of a given. test it with different number.
def greet():
    return "Hello, python learners!"
print(greet())

def square(num):
    x = num * num
    return x
print(square(5))
print(square(7))
print(square(9))

# Q2. function arguments & return values
# 2.1 write a function full_name(first, last) that takes first and last name as parameters and returns a singlestring in the format "First Last".
def full_name(first, last):
    return f"{first} {last}"
print(full_name("John", "Doe"))
# 2.2 write a function calculate_area(length, width = 10) that returns the area of a rectangle. test it by calling the function with:
# a. both length and width
# b. only length (use default width)
def calculate_area(length, width = 10):
    # area = length * width
    # return area
    return length * width

print(f"Area with both length and width: {calculate_area(5, 8)}")
print(calculate_area(5))

# Q3. Lambda functions
# 3.1 write a lambda function that adds two numbers and test it
# 3.2 create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.

sum = lambda a, b : a+b
print(sum(5, 8))

square = lambda x: x*x
list1 = [1, 2, 3, 4, 5]
print(list(map(square, list1))) # Output: [1, 4, 9, 16, 25]

# Q4. Recursion in python 
# 4.1 write a recursive function factorial(n) that returns the factorial of a given number 
def factorial(n):
    # base case
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))  
# factorial(5) = 5 * 4*3*2*1 = 120

# 4.2 write arecursive function sum_of_digits(n) that returns the sum of all digits of a given number n.
def sum_of_digits(n):
    # base case
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

# sum of digits or 7532 as
# 2 (last digit) + sum of digits of 753
print(sum_of_digits(7532))  # Output: 17

# Q5. modules and pip - using external libraries
# 5.1 import the math module and use it to 
# a. find the square root of 144
# b. calculate sin(90 degrees) (hint: use math.radians() to convert degrees to radians)

import math

a = math.sqrt(144)
b = math.sin(math.radians(90))
print(a, b ) # Output: 12.0 1.0

# 5.2 install import the requests module (if available) and use it to fetch data from "https://api.github.com" and print the status code of the response.

# import requests # pip install requests
# a = requests.get("https://api.github.com")
# print(a.json())  # Output: 200

# Q6. variable scope And Docstrings
# 6.1 write function increment() that has a local variable counter initialized to 0 and increments it by 1 each time it is called. observe the value persists across function calls.

def increment(): 
    counter = 0  # local variable
    counter += 1
    return counter
print(increment())  # Output: 1
print(increment())  # Output: 1
print(increment())  # Output: 1
print(increment())  # Output: 1
print(increment())  # Output: 1
# alwayes gives one, it will not persist across function calls,
# simply it will not goint to increment the


# 6.2 write a function multiply(a, b) that has a proper docstring explaining what it does, then use help(multiply) to display the docstring.

def multiply(a, b):
    """Returns the product of two numbers a and b."""
    return a * b
print(multiply(5, 3))  # Output: 15

# Q7. bonus Q.
# 7.1 Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers.
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_seq = fibonacci(n - 1)
        fib_seq.append(fib_seq[-1] + fib_seq[-2]) # here we are appending the last two elements of the list to get the next Fibonacci number
        # append is simply means to add an element to the end of the list
        return fib_seq
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]    

# 7.2 Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0.

def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(safe_divide(10, 2))  # Output: 5.0
print(safe_divide(10, 0))  # Output: Cannot divide by zero

# 7.3 Create a small module my_utils.py with a function is_even(n) that returns True if n is even. Import and use it in another Python file.
import my_utils
print(my_utils.is_even(4))  # Output: True