# Map filter and reduce

# map, filter, and reduce are higher-order functions in Python (and many other programming languages) that operate on iterables (lists, tuples, etc.). They provide a concise and functional way to perform common operations on sequences of data without using explicit loops. While they were more central to Python's functional programming style in earlier versions, list comprehensions and generator expressions often provide a more readable alternative in modern Python

# *** Map
# defination :- map, filter, and reduce are higher-order functions in Python (and many other programming languages) that operate on iterables (lists, tuples, etc.). They provide a concise and functional way to perform common operations on sequences of data without using explicit loops. While they were more central to Python's functional programming style in earlier versions, list comprehensions and generator expressions often provide a more readable alternative in modern Python

# numbers = [1, 2, 3, 45, 4, 21]

# def square(x):
#     return x * x
# # new = map(square, numbers)
# # print(new) #this will print, square applied in every element present in numbers, bute here is a cach this exact codes op will be "<map object at 0x0000013FEECA6410>" and this is how exact it works by default
# # just type castr it
# new = list(map(square, numbers))
# print(new)

# we can also use the syntex like this to avoid creating function

# #numbers = (2, 3, 4, 5, 6, 7)
# #new = list(map(lambda x: x*x, numbers))
# #print(new)

# *****Filter
# defination :- The filter() function constructs an iterator from elements of an iterable for which a function returns True. In other words, it filters the iterable based on a condition.

# def is_greater_than_9(x):
#     if x>9:
#         return True
#     else:
#         False
# a = [2, 4, 5, 78, 5, 7, 77, 789]
# # new = filter(is_greater_than_9, a)
# # print(new) # this return "<filter object at 0x0000022C42B263E0>" by default 


# # new = list(filter(is_greater_than_9, a)) #this can be 
# new = list(filter(lambda x: x>9, a)) #also write it like this 
# # some times avoid writing lamda functions if it's not readable or not able to maintain readablity
# print(new) # this return "<filter object at 0x0000022C42B263E0>" by default 

# ***reduce
# defination - The reduce() function applies a function of two arguments cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value. reduce is not a built-in function; it must be imported from the functools module.

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6] # add first two eliment from the list, 1+2 = 3 
#         [3, 3, 4, 5, 6] # 3+3 = 6
#         [6, 4, 5, 6] #6+4 = 10
#         [10, 5, 6] #10+5 = 15
#         [15, 6] #15+6 = 21
#         [21] # which is the O/P

def sum(a, b):
    return a + b

c = reduce(sum, numbers) #it takes (function, itrable)
print(c) # this will return 21, 

# application of a given function one by one to the all the values to the given list 

