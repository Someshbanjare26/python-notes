# Defining Functions in python

# the normal way to do a task, for example, calculating the average of three numbers
# a = 4
# b = 5
# c = 6

# avrg = (a + b + c)/3.0
# print("The average is:", avrg)

# a1 = 4
# b2 = 5
# c3 = 6

# avrg = (a1 + b2 + c3)/3
# print("The average is:", avrg)

# this will work for smaller programs, but what if we have larger programs like 50-60 lines of code then that will not goin to work here and to solve that we use functions

# the function defination
# def average(a, b, c):
#     d = (a + b + c) / 3.0
#     print(d)
# after runing this nothing will goin to happen because we have only defined the function but not called it

# def average(a, b, c):
#     d = (a + b + c) / 3.0
#     print(d)
# o1= average(4, 5, 6)  # calling the function with arguments 4, 5, 6
# o2=average(5, 9, 12)
# print(o1)
# print(o2) # the nothing will be printed here because the function does not return anything
# here we should use return statement instead of print 

def average(a, b, c):
    d = (a + b + c) / 3.0
    return d
o1 = average(4, 5, 6)  # calling the function with arguments 4, 5, 6
o2 = average(5, 9, 12)
print(o1)
print(o2)
# now this will work fine and we will get the output as expected
# note: a function should do only one task, if you want to do multiple tasks then you should define multiple functions