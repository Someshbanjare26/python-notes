# Variable Scope and Docstrings

'''
In Python, variables have scope 
(where they can be accessed) and lifetime (how long they exist).
Variables are created when a function is called and destroyed when it returns.
Understanding scope helps avoid unintended errors and improves code organization

'''

# def sum(a, b):
#     # a and b are local variables, they are only accessible within this function can not be accessed outside
#     c = a + b
#     return c
# print(sum(5, 3))  # Output: 8
# # print(c)  # Error: NameError: name 'c' is not defined

# what if i want to access everywhere in program
# def sum(a, b):
#     c = a + b
#     # print(z) # accessing global variable inside function
#     z = 1 #create a local variable called z which destroyed after this function returns,
#     return c

# z = 8 # global variable, can be accessed anywhere in the program
# print(sum(5, 3))
# print(z)  # you will print 8 not 1 


# global keyword
def sum(a, b):
    print("hey  im summing")
    c= a + b
    global z  # please modify the global variable z
    z = 0 # this will refer to global z and not create a local variables, it means now it create a global variable z
    return c 
z = 8
print(sum(5, 3))  # Output: 8
print(z)  # Output: 0

# A Q. occurs here, can you modify a global variable inside a function 
# the ans is, yes but we'll have to use global keyword for that

#  Docstrings - Writing Function Documentation
'''
Docstrings are used to document functions, classes, 
and modules. In Python, they are written in triple quotes. 
They are accessible using the __doc__ attribute.
Here's an example:

'''

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b
 
print(add.__doc__)  # Output: Returns the sum of two numbers.

# onother detailed example
def add(a, b):
    """
    Returns the sum of two numbers.
 
    Parameters:
    a (int): The first number.
    b (int): The second number.
 
    Returns:
    int: The sum of the two numbers.
    """
    return a + b

'''
Summary
  . Functions help in reusability and modularity.
  . Functions can take arguments and return values.
  . Lambda functions are short, inline functions.
  . Recursion is a technique where a function calls itself.
  . Modules help in organizing code and using external libraries.
  . Scope and lifetime of variables decide their accessibility.
  . Docstrings are used to document functions, classes, and modules.

'''