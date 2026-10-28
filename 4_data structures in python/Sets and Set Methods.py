# Sets and Set Methods
# Sets are unordered, unique collections (no duplicates).

# s = {1, 2, 3, 4, 5}
# print(s, type(s))
# you can not access elements of set by index becouse sets are 
# so --> print(s[2])  # this will raise an error

# set methods
s = {1, 2, 3, 4, 5}
print(s)

# add() method - adds an item to the set
s.add(6)  # {1, 2, 3, 4, 5, 6}
print(s)
# remove() method - removes a specified item from the set
s.remove(3)  # {1, 2, 4, 5, 6}
# discard() method - removes a specified item from the set (does not raise an error if item not found)
# suppose we want to remove an item which is not present in the set
# s.remove(10)  # this will raise an error, but if we use discard() method it will not raise an error
s.discard(10)  # no error
# pop() method - removes random item from the set (not always used)

# set operations

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# union() method - returns a set containing all items from both sets
c = a.union(b)  # {1, 2, 3, 4, 5, 6}, no repeatation is allowed here 
print("Union:", c)

# intersection() method - returns a set containing only items that are present in both sets
d = a.intersection(b)  # {3, 4}
print("Intersection:", d)

# difference() method - returns a set containing items that are in the first set but not in the second
e = a.difference(b)
print("Difference:", e)  # {1, 2}






