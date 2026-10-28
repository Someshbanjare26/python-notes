# Lambda Functions in Python
# Lambda functions are anonymous, inline functions.
# it just use for convienience when you need a small function for a short period of time.

square = lambda x: x * x
sum = lambda a, b: a + b
print(square(5))  # Output: 25
print(sum(3, 7))  # Output: 10


'''
as good as writing:
def sum(a, b):
    return a + b
'''



