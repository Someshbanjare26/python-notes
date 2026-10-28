# List Methods
# creating a list

marks = [85, 85, 90, 78, 92, 88]
print(marks)
# append() method - adds an item to the end of the list
marks.append(95) # [85, 90, 78, 92, 88, 95]
# insert() method - adds an item at a specified index
marks.insert(2, 80) # [85, 90, 80, 78, 92, 88, 95]
# pop() method - removes and returns the last item or item at specified index
marks.pop() # removes 95
# remove() method - removes the first occurrence of a specified value
marks.remove(78) # [85, 90, 80, 92, 88]
# sort() method - sorts the list in ascending order
marks.sort() # [80, 85, 88, 90, 92]
# reverse() method - reverses the order of the list
marks.reverse() # [92, 90, 88, 85, 80]
# count() method - returns the number of occurrences of a specified value
marks.count(85) # returns 1
# index() method - returns the index of the first occurrence of a specified value
marks.index(90) # returns 1
# if we want access the element of list by using index
print(marks[2]) # prints 88
# length of the list
print(len(marks)) # prints 5

# you can learn more about list methods in python from the official documentation

# list comprehension  <--

# for example we are performing :
# a = 5
# table = []

# for i in range(1, 11):
#     table.append(a * i)
# print(table)  # prints [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]    

# this can be done by using list comprehension in just one line
table = [5*i for i in range(1, 11)]
print(table)  # o/p --> [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]    







