# Python Basics - Practice Set 

#1. Write a program that prints:
# Hello, World! Welcome to Python.
print("Hello, World! Welcome to Python.")

'''
2. Write a program that prints the following poem using a single print() statement:

(Hint: Use \n for a new line.)

Twinkle, twinkle, little star,
How I wonder what you are!

'''
print("Twinkle, twinkle, little star,\n How I wonder what you are!")

# 3.  Variables & Data Types
# Create variables to store:

# Your name (string)
# Your age (integer)
# Your height in meters (float)
# A boolean value representing whether you are a student
# Print all of them in one line.

name = "Sonu"
age = 20
height = 6.0
student = True
# print("my name is :", name, "\n my age is :", age, "\n my heiht is :", height, "\n i am student ?", student )
print("my name is :"+ name + " my age is :"+ str(age) + " my heiht is :" + str(height) + " i am student ?", student ) # \n is not required becouse we have to solve a Q. as it ment to be 

# Q4: Typecasting Practice
# You are given a string:
#a. Convert it into an integer
#b. Add 10 to it
#c. Print the result

num = "45"
print(int(num) + 10)  # Output: 55

# Q5: Taking User Input
# Write a program that:

# Asks the user for their favorite food.
# Prints:
# Wow! I also like <food>

info = input("what is your favorite food ? :")
print("Wow! I also like", info)
print("Wow! I also like" + info)


# Q6: Simple Calculator
# Write a program that:

# Takes two numbers as input from the user.

# Prints their:

# Sum
# Difference
# Product
# Quotien

a = (int(input("Enter the first number : ")))
b = (int(input("\nEnter the second number : ")))
print("a + b is ", a+b)
print("a - b is ", a-b)
print("a * b is ", a*b)
print("a / b is ", a/b)


# Q7: Escape Sequences
# Print the following output using escape sequences:

# Hello "Python" World!
# This is on a new line.
# This is a tab →	    after tab

print('Harry said, "Python is awesome!" \nThis is on a new line. \nThis is a tab ->\t<- here')


# Q8: Operator Challenge
# Write a program that:

# Takes an integer as input from the user.
# Prints the square and cube of that number.

a = (int(input("Enter any number: ")))
# print(a*a, + a*a*a)
print("Square is", a**2)
print("cube is", a**3)