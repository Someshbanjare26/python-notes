# Recursion in Python
# A function calling itself to solve a problem.

'''
fibonachi sequence:
0 1 1 2 3 5 8 13

fib(0) = 0
fib(1) = 1
fib(2) = fib(0) + fib(1) 
fib(3) = fib(1) + fib(2) 
fib(4) = fib(2) + fib(3) 
fib(5) = fib(3) + fib(4) 
fib(n) = fib(n-2) + fib(n-1) 

'''
def fib(n):
    # base case
    if(n == 0 or n == 1):
        return n
    return fib(n-2) + fib(n-1)
print(fib(7))  # Output: 13

# explaimination & working of this behind the scene
# 0   1   1   2   3   5   8   13
# |   |   |   |   |   |   |    |
# f0  f1  f2  f3  f4  f5  f6   f7

# fib(5)
# = fib(3) + fib(4)
# = (fib(1) + fib(2)) + (fib(2) + fib(3))
# = (fib(1) + (fib(0) + fib(1))) + ((fib(0) + fib(1)) + (fib(1) + fib(2)))
# = (1 + (0 + 1)) + ((0 + 1) + (1 + (0 + 1)))

# be very careful while using recursion
# if you avoid base case it will go to infinite recursion and give RecursionError, and also your pc can crash.
# it can also be called as something like infinite recursion 



