# Exception Handling and Custom Errors

# while True:
#     try:
#         a = int(input("Enter number 1: "))
#         b = int(input("Enter number 2: "))
#         print(f"The sum is {a+b}")
#         # yu can also use except for any specific kind of error, for example 
#     except ValueError:
#         print("please don't perform bad typecast ")
#     except ZeroDivisionError:
#         print("hey dont divide by 0")
#         # the exception given bellow is a universal kind of thig we can use it for any thing  
#     except Exception as e:
#         print("Some error occurred!", e)

# # try & excpet are used to handle the error  in python, for example if use type string insted of integer then program get get crashed but after using this megthord the program keep working without any issue


# ****somtimes we want to rais an error 

# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))

# if b ==0:
#     raise ValueError("polease don't divide by 0")

# print(f"The division is {a/b}")

# ****** else & finally
# ****else

# try: 
#     # a = 345/0 
#     a = 345/10 
# except Exception as e: 
#     print(e) #n don't put f string her it will throw NameError


# else: 
#     print(f"hey i am good {a}")# this will exicute when ther is no error

# let suppose you want to run the program alwasy, it migth have error or it migth have no error

# ***fianlly

a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

try:
    c = a/b
    print(c)

except Exception as e:
    print(e)

finally:
    print("this is always exicuted")

# we can also do like given bellow so why we use finally keyword, here if we rap ervery thing inside a function then we try to exicute it will exicute only there will be a "finally" key word is used 
# print("this is always exicuted")
