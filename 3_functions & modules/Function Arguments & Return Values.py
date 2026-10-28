# Function Arguments & Return Values

# def add(a, b): # a and b are simply variable name which are called function parameters
#     return a+b
# c = add(5, 3) # 5 and 3 are the arguments passed to the function, it means the value which actually passed is call arguments
# print("Sum:", c)  # Output: Sum: 8

# # types of arguments
# # 1. Positional Arguments
# # it s what we saw in the above example
# # 2. default Arguments
# # which contains default values
# def add(a1, b1, plus = 0): # after the possitional arguments we put defoult argument, this thing optional 
#     x =  a1 + b1 + plus
#     return x
# c= add(5, 3, 2) # here plus will take default value 0
# print(c) # Output: 10

# 3. keyword Arguments
# when i am mentioning which value is metioned to which parameter
def add(a1, b1):
    x =  a1 + b1
    return x
c= add(b1=3, a1=5) # here plus will take default value 0
print(c) # Output: 8
# onother example
def student(name, age):
    print(f"Name: {name}, Age: {age}")
 
student(age=20, name="Bob")