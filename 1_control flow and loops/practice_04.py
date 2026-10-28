# Break, Contoinue and Pass Statements in Python

# Break Statement Example

for i in range(0, 21):
    print(i)
    if i == 11:
        break # cancel the loop when the condition is met
# kehane ka matlab hai ki jab i ki value 11 ho jaye to loop ko rok do

# Continue Statement Example

for i in range(1, 20):
    if i == 11:
        continue # skip the current iteration when the condition is met
    # kehane ka matlab hai ki jab i ki value 11 ho jaye to is iteration ko skip kar do
    print(i)
#  11 skip ho jayega aur baki sab print hoga

# Pass Statement Example

i = 3

if i == 23:
    pass # do nothing, just a placeholder
print("End of program")







