# practice_02
name = "sonu12345678098"


print(name[0:2]) # it will print characters from index 0 to 1 which is "so", goes from 0 to 2-1ie 0 to 1 
print(name[2:-1]) # same goes as name[2:4] which is "nu"

print(name[0:10:1]) # skip 1 character while slicing 
print(name[0:10:3]) # skip 3 character while slicing, 3-1 ie 2 characters

print(name[:2]) # it will print from starting to index 1 which is "so" # same as name[0:2]
print(name[2:]) # it will print from index 2 to end which is "nu12345678098" # same as name[2:len(name)]

# The syntax ::2 is a slice notation [start:stop:step] where the start and stop are omitted (meaning default to the entire string) and the step is set to 2. 