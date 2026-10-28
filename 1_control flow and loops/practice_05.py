# python conditional & loops - practice set


#PS 1 - using If-Else Conditional Statements
 
# PS 1.1 - Write a program that asks the user for a number and prints whether it is positive, negative, or zero

# logic 
from unittest import case

from regex import match


num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# PS 1.2 - create a program to cheaks if a person is eligible to vote (age => 18) 
   
age  = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
elif age < 18:
    print("You are not eligible to vote yet.")
else:
    print("Invalid age entered.")


# PS 1.3 - Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd"
number = int(input("Enter a number: "))
if(number % 2 == 0):
    print("Even")
else:
    print("odd")

# PS 2 -  Match Case Statements

# PS 2.1 Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case 

day_num = int(input("Enter a day number (1-7): "))
match day_num:
    case 1:
        print("sunday")
    case 2:
        print("monday")
    case 3:
        print("tuesday")
    case 4:
        print("wednesday")
    case 5:
        print("thusday")
    case 6:
        print("friday")
    case 7:
        print("satuday")
    case _:
        print("pleas enter the number in between 1-7")

# PS 2.2 - Write a program using "match case " that simulates a simple calculator. 

# 1. Ask the user for two numbers and an operation(+, -, *, /)
# 2. Perform the operation using match case.

num_1 = int(input("Enter first number: "))
num_2= int(input("Enter second number: "))
operation = input("Enter an operation (+, -, *, /): ")
match operation:
    case "+":
        print(num_1 + num_2)
    case "-":
        print(num_1 - num_2)
    case "*":
        print(num_1 * num_2)
    case "/":
        print(num_1 / num_2)
    case _:
        print("Invalid operation")    


# PS 3 - For Loops
# PS 3.1 - print number from 1 to 10 using for loop

for i in range(1, 11):
    print(i)


# PS 3.2 - print the multiplication table of a number entered by the user
num = int(input("Enter a number to print its multiplication table: "))
for i in range(1, 11):
    print(num,"X", i, "=", num * i)
    

# PS 3.3 - calculate the sum of all numbers from 1 to 100 using a for loop

sum = 0
for i in range(1, 101):
    sum += i 
print("The sum of all numbers from 1 to 100 is:", sum)

# PS 3.4 - print the following pattern using a for loop
# *
# **
# ***
# ****

for i in range(1, 5):
    print("*" * i)


# PS 4 - While Loops
# PS 4.1 - Write a program that prints the numbers from 1 to 10 using a while loop

count = 1
while count <= 10:
    print(count)
    count += 1



# PS 4.2 - Write a program that keeps asking user to enter a password until they enter the correct one.

password = "Somesh26#"
user_input = input("Enter the password: ")
while user_input != password:
    print("Incorrect password. Try again.")
    user_input = input("Enter the password: ")

print("Access granted.")

# PS 4.3 - Write a program to reverse a given number 

num = 546
print(int(str(num)[::-1])) # advance slicing 

# PS 5 - break, continue and pass statements 
#  do this 







