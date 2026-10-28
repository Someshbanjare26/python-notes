# Python Collections – Practice Set

# Introduction list:
# Q1. create a list fruits = ["apple", "banana", "cherry"]
# 1.1 print the first fruit
# 1.2 replace "banana" with "orange"
# 1.3 print the length of the list

# fruits = ["apple", "banana", "cherry"]
# print(fruits)
# print(fruits[0])
# fruits[1] = "orange"
# print(fruits)
# print(len(fruits))

# # create a list of numbers from 1 to 10
# # 1.1 print the frist three numbers using slicing
# # 1.2 print the last three numbers using slicing

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(num[0:3])
# print(num[7:10])
# print(num[-3:])

# List Methods
# Q1. start with numbers = [5, 2, 9, 1, 7] and do following things:
#   1.1 Srt the list in assending order
#   1.1 Srt the list in decending order
#   1.2 Apend the number 10 to the list 
#   1.3 Rmove the number 2 from the list 

# numbers = [5, 2, 9, 1, 7]
# numbers.sort()
# print("number is sorted in ascending order:", numbers)
# numbers.sort(reverse=True)
# print("number is sorted in descending order:", numbers)
# numbers.append(10)
# print("number is Append :",numbers)
# numbers.remove(2)
# print("2 i removed from the list :",numbers)

# # Q. create a list names = ["Alice", "Bob", "Charlie"] and use the insert() methord to add "devid" at index 1.
# names = ["Alice", "Bob", "Charlie"]
# names.insert(1, "devid")
# print(names)

# ---> Tuples and Operations on Tuples
# 1.1 create a tuple coordinates  = (10, 20) and print both elements.
# 1.2 try modify the tuple by setting coordinates[0] = 50 -- note what that happend
# 1.3 convert the tuple to a list, changing its first element to 50,  and conver it back to a tuple 
coordinates = (10, 20)
# print(coordinates)
print(coordinates[0])
print(coordinates[1])

# coordinates[0] = 50 # TypeError: 'tuple' object does not support item assignment
# print(coordinates)

# coordinates[0] = 50
corlist = list(coordinates)
corlist[0] = 50
# print(tuple(corlist)) # also you can do like given bellow :-

# Sets and Set Methods
# 1.1 Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3?)
# 1.2 add 5 to set, remoiovinng 2, and check if 4 is in the set
#create two sets: 
#  a = {1, 2, 3}
#  b = {1, 2, 3}
# find their :
# union 
# intersections 
# Difference (a - b)

# my_set = {1, 2, 3, 3, 4} 
# print(my_set) # after printing 3 will be removed becouse of set proiperties 
# my_set.add(5)
# my_set.remove(2)
# print(my_set)

# a = {1, 2, 3}
# b = {3, 4, 5}
# # a.union(b)
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))

# Q. 5. Dictionaries and Dictionary Methods
# 1.1  create a dictionary student = {"name": "John", "age": 20, "grade": "A"}
#    . print the valuie of "name"
#    . change "grade" to "A+"
#    . Addd a new key "city" with value "Delhi"

student = {"name": "John", "age": 20, "grade": "A"}
print(student["name"])
# student.update({"grade": "A+"})
student['grade'] = "A+"
print(student)
# student.update({"city": "Delhi"})
student["city"] = "Delhi"
print(student)

# 2.1 create a dictionary of three friends and their phone numbers. Use
#      .keys() to get all numbers
#      .values() to get all numbers
#      .items() to loop over key-values pair and print them

my_dic = {
    "sonu": 9090909090,
    "rohan": 9090909091,
    "chintu": 9090909092,
}
# print(my_dic.keys())
# print(my_dic.values())
# print(my_dic.items())
# also you can
for key, value in my_dic.items():
    print(key, value)

# bonus Q.
# Write a program that takes a list of numbers and removes all duplicates using a set.
num1 = input("enter the first list of numbers :")
num2 = input("enter the second list of numbers :")
print(num1.union(num2))

# do the other three Questions 




