# practice_04
# String Formatting 

# template = "Dear sonu, you are awesome. thake this 10000$ bag"

# a = "john"
# a1 = 10000
# b = "jack"
# b1 = 1000
# c = "maria"
# c2 = 3000

# first option is to type manualy 
# but we have second option using format method

template = "Dear {}, you are awesome. thake this {} bag"
a = "john"
a1 = 10000
b = "jack"
b1 = 1000
c = "maria"
c2 = 3000

s1 = template.format(a, a1)
print(s1)
# this was a basic example of format method
# best way is to use f-strings
# f-strings 
print(f"{a} you are awsome and take this {a1}$ bag")

# there more funtions like that will not goin to use to much but only some time you will need them some exapmples are given below
# charector encoding
# ord() - gives the unicode/askey of a character
# chr()- gives the character of a unicode/askey value
# you can also refor unicode table from the internet
