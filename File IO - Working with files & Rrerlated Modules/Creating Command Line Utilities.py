# Creating Command Line Utilities
'''
You can use Python to create simple command-line utilities. The argparse module makes it easier to handle command-line arguments.

'''
# argparse

import argparse

parser = argparse.ArgumentParser(description="simple calculator")

parser.add_argument("num1", type=float, help="first number")
parser.add_argument("num2", type=float, help="second number")
parser.add_argument("operation", choices = ["add", "sub" , "div", "mul"], help="Operation to perform")

args = parser.parse_args()

# print(args)

if(args.operation == "add"):
    print(f"The result is {args.num1 + args.num2}")
elif(args.operation == "sub"):
    print(f"The result is {args.num1 - args.num2}")
elif(args.operation == "mul"):
    print(f"The result is {args.num1 * args.num2}")
elif(args.operation == "div"):
    print(f"The result is {args.num1 / args.num2}")
else:
    print("somthings wrong")