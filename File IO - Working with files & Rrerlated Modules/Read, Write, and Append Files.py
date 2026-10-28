# Read, Write, and Append Files

'''
Python provides several modes for opening files:

'r' (Read mode): Opens the file for reading. This is the default mode. If the file doesn't exist, you'll get an error.
'w' (Write mode): Opens the file for writing. If the file exists, its contents will be overwritten. If the file doesn't exist, a new file will be created.
'a' (Append mode): Opens the file for appending. Data will be added to the end of the file. If the file doesn't exist, a new file will be created.

'''
# very importent thing is to close the file when it ges open

# f = open("sonu.txt", "rt") # r --> read karo, t --> text mode me, if there were b insted of t, b --> in binary mode
# f = open("sonu.txt", "r") # we can use only r coz t is by default present, we use b only when we are wiiling to read in binary mode
# # if the above code is note working, try this
# # Replace line 14 with the absolute path
# # f = open(r"C:\coding_stuff\Complete_DataScience\completePython_CWH\programs\File IO - Working with files & Rrerlated Modules\sonu.txt", "r")
# content = f.read()
# print(content)
# f.close() # this function will close the file after reading it

# writing 
# f = open("kalpana.txt", "w")
# string = '''
#  kalpana have most the beutifull eyes i have ever seen  
# '''
# f.write(string)

# f.close

# append

# f = open("chulbuli.txt", "a")
# string = '''
#  chulbuli loves me so much hav't decleared rn   
# '''
# f.write(string)
# f.close()

# there is a cool way to read the file, thater than this treditional way 

# f = open("sonu.txt", "rt")
# content = f.read()
# print(content)
# f.close()

# we can simpley way do like this 
# with open("chulbuli.txt", "r") as f: # context manager
#     content = f.read()
#     print(content)
#     # no need to write f.close ()(becouse file is already closed by defoult)


