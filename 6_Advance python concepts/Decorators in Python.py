# Decorator is a function that takes a function, it create a new function inside its body (wrapper ). then it returns thate new function

# def decorator(func):
#     def wrapper():
#         print (" I am about to execute a function...")
#         func()
#         print("I have executed this function...")
#     return wrapper 

# def say_hello():
#     print("hello!")

# f = decorator(say_hello)
# f()

# here we can see how this "f()" will look while the execution of the code 
# def f():
    # print(" I am about to execute a function...")
    # print("hello!")
    # print("I have executed this function...")

# there is alternative syntex to write decorators, which is given below


# def decorator(func):
#     def wrapper():
#         print (" I am about to execute a function...")
#         func()
#         print("I have executed this function...")
#     return wrapper 

# @decorator
# def say_hello():
#     print("hello!")

# say_hello()

# f = decorator(say_hello)
# f()
# Here, @decorator is syntactic sugar for f = decorator(say_hello). It modifies the behavior of say_hello() by wrapping it inside wrapper(). The wrapper function adds behavior before and after the original function call.


# **** Using Decorators with Arguments

def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def say_hello(a):
    print(f"hello {a}")


'''
it replaces the function sy_hello with this:
def decorator(func):
    def wrapper(a):
       fro i in range(n):
           say_hello(a)
    return wrapper
'''

say_hello("sonu")

    











