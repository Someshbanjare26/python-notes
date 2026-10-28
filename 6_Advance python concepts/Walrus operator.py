# defination -  The walrus operator (:=), introduced in Python 3.8, is an assignment expression operator. It allows you to assign a value to a variable within an expression. This can make your code more concise and, in some cases, more efficient by avoiding repeated calculations or function calls. The name "walrus operator" comes from the operator's resemblance to the eyes and tusks of a walrus.
# Walrus operator helps to reduce some useless repeated calculation/code

def very_slow_func():
    print("Somthing...") 
    print("Somthing...") 
    print("Somthing...") 
    print("Somthing...") 
    print("Somthing...") 
    # return 10 # but if i'll write 70 isted of 10
    return 70 # the O/P returns it twis, to avoid this kind of shit we use warlus operator
# to avoid this repeatation in O/P we can optemize the code while asign it with an operator
# if(very_slow_func()>10):
#     print(very_slow_func())
# else:
#     print("its not greater than 10")
# a = very_slow_func() 
# if(a>10):
#     print(a)
# else:
#     print("its not greater than 10")
# now the O/P will not be repeating,  apart from this we can use Walrus operator since it is better way

# if((a:=very_slow_func())>10):
#     print(a)
# else:
#     print("its not greater than 10")
# # not just returning it once we are also storing the value in "a" 

# *** Let see some simple usecases

while(data:=input("Enter the value: ")):
    print(data)
    if data == "q":
        break
# the program break when input is "q", untill it will keep asking for value








