# Method Overriding and Operator Overloading
class point:
    def __init__(self, x, y):
        self.x = 1
        self.y = 2
    def sum(self, p):
        return point((self.x + p.x), (self.y + p.y))
    
    def print_point(self):
        print(f"X is {self.x} and Y is {self.y}")

    def __add__(self, p):
        return point((self.x + p.x), (self.y + p.y))
    
p1 = point(3, 2)     
p2 = point(6, 3)     

# p = p1.sum(p2)
# p.print_point()

# Operator Overloading

p = p1 + p2
p.print_point()



# Other useful magic methods: (You don't need to memorize them all, but be aware they exist!)

# __sub__ (-), __mul__ (*), __truediv__ (/), __eq__ (==), __ne__ (!=), __lt__ (<), __gt__ (>), __len__ (len()), __getitem__, __setitem__, __delitem__ (for list/dictionary-like behavior – allowing you to use [] with your objects).





