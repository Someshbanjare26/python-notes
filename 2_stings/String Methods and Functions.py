# practice_03
# String Methods and Functions
# strings are immutable in python

# name = "sonu"

# # name[0] = "R" # you can not do this, it throws typeError: 'str' object does not support item assignment

# # string methords

# a = len(name) # len() function returns length of the string
# print("Length of name is:", a)  


# commomn string methord

s = "hello world"

# s[0] = R # you can not do this 

a = len(s)
print(a)
print(s.upper(), s) # you will see that the actuall strind does not changed, but the upur case of that string is saved in memory 
print(s.lower(), s)
print(s.capitalize(), s)
print(s.title(), s) # pehala letter har ek word ka jo hai vo capital  me rahega
# we have multiple function like
# strip() lstrip() rstrip() - to remove spaces
# find() - to find a substring
text = "sonu is nice man "
print(text.find("is") )# output: 5 index of first occurence of substring
# replace() - to replace a substring with another substring
print(text.replace("is", "look like,",) )
# if i want to replace two words in one go i will do it like this
print(text.replace("sonu", "kalpana").replace("man", "women") )

# split() - to split a string into a list of substrings
text2 = "sonu,kalpana,rohan"
print(text2.split(",")) # it will split the string at every comma and return a list of substrings
# join() - to join a list of strings into a single string
print(",".join(["sonu", "kalpana", "rohan"])) # it will join the list of strings with comma in between

# count() - to count occurrences of a substring
# startswith() - to check if a string starts with a specific substring
# more yu can explore in python documentation, in notebook of string methods and functions i have added more methods with examples
# some examples which give output as boolean are shown below
# isalpha() - to check if all characters in the string are alphabetic
# isdigit() - to check if all characters in the string are digits
# isalnum() - to check if all characters in the string are alphanumeric
# isspace() - to check if all characters in the string are whitespace
