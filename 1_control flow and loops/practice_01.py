# Match Case Statments in python

a = int(input("Enter a number between 1 to 10: "))

match a:
    case 1: # if input se ye cose match ho jati hai to ye exicute hoga, nai to age bad jayega
        print("You won a laptop")
    case 2:
        print("You won a mobile")
    case 3:
        print("You won $3")
    case _: # if koi bhi case match nai hota to ye default case chal jayega 
        print("better luck next time :) ")


# itis similor to if else stament but match case statements are very convinient and strait forword thats why we are using it, it was introduced in python 3.1.0




