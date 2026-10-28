# Tuples and Operations on Tuples
# Tuples are ordered but immutable collections (cannot be changed after creation).

my_tuple = (10, 20, 30, 40, 50)
mixed_tuple = (1, "World", 2.71, False)

# Accessing elements
print(my_tuple[1])  # prints 20
print(20)

# creating a tuple with a single element
# tupl = (5) # This is not a tuple, becouse parentheses are used for grouping
# in list = [5] # this is allowed becouse square brackets are used for list creation
tuple = (5,)  # This is a tuple, you should always add a comma for single element tuple

# tuple unpacking
tu = (1, 2, 3)
a, b, c = tu
print(a, b, c)
# tuple unpacking is simpler way to assign values to multiple variables in one line
# it can also be defined as unpacking of tuple elements into individual variables
# where we assign certain number of variables to the elements of the tuple in the same order

# tuples methods
# since tuples are immutable they don't have many methods like lists
# but still we have some methods for tuples
# count() method - returns the number of occurrences of a specified value
tu = (1,2,21,3,2,4,2)
print(tu.count(2))  # prints 3
# index() method - returns the index of the first occurrence of a specified value
print(tu.index(2))  # prints 1


# Why Use Tuples?
#  .Faster than lists (since they are immutable)
#  .Used as dictionary keys (since they are hashable)
#  .Safe from unintended modifications