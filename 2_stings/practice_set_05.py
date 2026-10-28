#plese do the practice set first from string notes

# Q.1) create a string variable name withw your full name and print:
# a) the first charecter
# b) the last charecter 
# c) the length of the string

# name = "sonu"
# print(name[0])
# print(name[3])
# print(len(name))

# 1.1) concatinate two string : "hello" and "world" with a space in between and print it

# # print("hello" + " " + "world")
# str1 = "hello"
# str2 = "world"
# # print(str1 + str2) // it will print helloworld
# print(str1 + " " + str2) # it will print hello world
# print(str1,str2)# it will also print hello world 

# # Q2) string slicing and indexing
# # 1. give text = "python programing", do the following :
# #    a). print the first 6 charecters 
# #    b). print the last 6 charecters
# #    c). print every second charecter from the string

# tex = "python programing"
# print(tex[0:6])
# print(tex[-6:])
# print(tex[::2]) 
# # The syntax ::2 is a slice notation [start:stop:step] where the start and stop are omitted (meaning default to the entire string) and the step is set to 2.
# #  2.2) reverse the string "python programing" and print it

# print(tex[::-1]) # this will reverse the string
# 4:50 time stamp

# Q3) String methods and functions 
# 1. take the string "   i love python programming   " and 
#    a). remove the extra spaces from the start and the end and print it
#    b). convert it to title case
#    c). count how many times the word "o" appears

# text = "   i love python programming   "
# print(text.strip())
# print(text.title())
# print(text.count("o"))
# # 3.1) check if the string "123abc" is alphanumeric 

# str1 = "123abc"
# # print(str1.isalnum())
# if str1.isalnum():
#     print("string is alphanumeric")
# else:
#     print("string is not alphanumeric")

# input("enter any alphanumaric string: ")
# user_input = input()
# if user_input.isalnum():
#     print("string is alphanumeric")
# else:
#     print("string is not alphanumeric")


# Q4) string formatting and f-string 

# 1. using formate(), create a sentence
# "my name is john and i am 20 years old"
# by paasing "john" 25 as variables
# 2. do the same using f-string

# name = "john"
# age = 25
# print("my name is {} and i am {} years old".format(name, age)) # formatting 

# print(f"my name is {name} and i am {age} years old") # f-string

# Q5) string manuputlation challenge
# 1. given sentance = "coding in python is fun", replace "fun" with "awesome" and print the new sentance
# 2. find the index of the "python" in sentance 
# 3. convert the entire sentance to uppercase and print it

sentance = "coding in python is fun"
print(sentance)
print(sentance.replace("fun", "awesome"))
print(sentance.index("python"))
print(sentance.upper())

# Q6) bonus challenge
# 1. write a program that counts how many vowels are there in a given string
# 2. take a user input string and check if it is a palindrome or not(same forwards and backwards)

str1 = "This is a sample string to count vowels"
print(str1)
print("Number of vowels in the string: ", str1.count("aeiouAEIOU"))
user_input = input("Enter a string to check for palindrome: ")
if user_input == user_input[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
