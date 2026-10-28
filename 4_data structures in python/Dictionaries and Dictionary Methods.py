# Dictionaries and Dictionary Methods
# Dictionaries store key-value pairs and allow fast lookups.

marks = {"sonu": 95, "jack": 39, "lily": 85}
print(marks,type(marks))

# you can store any data type(as key, as value), but that data type must be hashable (immutable)
# student = {"name": "Alice", "age": 21, "grade": "A"}

# Accessing dictionary
print(marks["sonu"])  # Output: 95

# dictionary aslo has lots of methods 

# also you can change content of dictionary
marks["sonu"] = 98 # updating value of key 'sonu'

# Accessing & Modifying Values:

# print(student["name"])  # Output: Alice
# student["age"] = 22     # Updating value
# student["city"] = "New York"  # Adding new key-value pair

# Common Dictionary Methods:
print(marks.keys())
print(marks.values())
print(marks.items())
print(marks.get("jack"))  # Output: 39
marks.pop("lily")  # Removes key 'lily'
marks.update({"jack": 45, "mike": 88})  # Updates 'jack' and adds 'mike'
marks.clear()  # Empties the dictionary
print(marks)

# dictionary comprehension
table_of_5 = {i: i*5 for i in range(1, 11)}
print(table_of_5)


# 5. When to Use Each Data Structure?
#  .Data Structure	Features	Best For
#  .List	Ordered, Mutable	Storing sequences, dynamic data
#  .Tuple	Ordered, Immutable	Fixed collections, dictionary keys
#  .Set	Unordered, Unique	Removing duplicates, set operations
#  .Dictionary	Key-Value Pairs	Fast lookups, structured data
