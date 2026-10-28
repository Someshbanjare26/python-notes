# defination - *args and **kwargs are special syntaxes in Python function definitions that allow you to pass a variable number of arguments to a function. They are used when you don't know in advance how many arguments a function might need to accept.

# *args: Allows you to pass a variable number of positional arguments.
# **kwargs: Allows you to pass a variable number of keyword arguments.

# arguments = args
# keyword arguments = kwargs

# if we have function
# def sum(a, b):
#     return(a+b)
# print(sum(234, 2))
# but what  is do 
# print(sum(234, 2, 7)) # ---> it will throug an error,  we can fix it using args

# def sum(*args):
#     # args takes every argument and create tuples it mesans args will be a tuple of all the values passed to sum
#     total = 0
#     for item in args:
#         total += item 
#     return total 

# print(sum(234, 64, 7)) # we can now do multiple  of sum 


# **** kwargs (Keyword Arguments)

# defination : - collects any extra keyword arguments passed to a function into a dictionary. Again, kwargs is the conventional name, but you could use any valid variable name preceded by two asterisks (e.g., **data, **options).

# def marks(**kwargs):
#     # kwargs is adictionary with all the key value pairs which were passed to marks
#     for item in kwargs.keys():
#         print(f"The marks of {item} is {kwargs[item]}")

# marks(shubham = 34, rohan = 54, chintu= 90, damni = 40)

# there is a special case where we can combine args and kwargs, thetre is a condition we have to use args first then kwargs after that

# def func1(*args, **kwargs):
#     print(args)
#     print(kwargs)

# func1(1, 2, 3, 5, jack =34, jill = 32, manshu = 31)
