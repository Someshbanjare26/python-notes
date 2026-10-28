# Python File Handling & Utilities – Practice Set


# 1 - 1. File I/O Basics
# Q. 1.1 - Create a text file notes.txt using Python and write "Learning Python is fun!" into it.

# f = open("notes.txt", "w")
# string = '''
#  Learning Python is fun!
# '''
# f.write(string)
# f.close

# ======= unother way 
# with open("notes.txt", "w") as f:
#     f.write("it' fun")



# Q. 1.2 - Open notes.txt, read its content, and print it to the console.

# f = open("notes.txt", "r")
# content = f.read()
# print(content)
# f.close()

# ======= unother way 

# 2 -  Read, Write, and Append Files

# Q2.1 -  Write a program that writes three lines of text to a file tasks.txt

# with open("notes.txt", "w") as f:
#     f.write("line1\n")
#     f.write("line2\n")
#     f.write("line3\n")


# Q2.2 - Open tasks.txt in append mode and add a new line "Task Completed!"

# with open("notes.txt", "a") as f:
#     f.write("task completed")

# Q2.3 - Read the file and print all lines as a list using readlines()

# with open("notes.txt", 'r') as f:
#     for line  in f.readlines():
#         print(line)


# 3 - OS and Shutil Modules
#Q3.1 - Use the os module to:
'''

Print the current working directory
List all files and folders in the current directory
Create a new folder my_folder 

''' 

# import os

# print(os.getcwd())
# print(os.listdir())
# os.mkdir("My_folder")



#Q3.2 - Use the shutil module to:
'''

Copy a file from one folder to another
Move a file to a new folder
Delete a file (careful: irreversible!)

''' 
# import shutil
# import os

# # shutil.copy("tasks.txt", "My_folder/taskes.txt")
# # shutil.move("tasks.txt", "My_folder/taskes.txt")
# os.remove("this.txt")

# 4 - Creating Command Line Utilities
#Q 4.1 - Write a small script count_lines.py that takes a filename as input and prints how many lines are in the file.Example usage:

# import sys
# def count_lines(filename):
#     with open(filename) as f:
#         return len(f.readlines())

# if __name__ == "__main__":
#     filename = sys.argv[1]
#     num_lines = count_lines(filename)
#     print(f"There are {num_lines} lines in {filename}")


#Q 4.2 -
'''
Write a command-line utility search_word.py that takes two arguments:

A filename
A word to search and prints how many times the word appears in the file.

''' 
# import sys
# def search_word(word, string):
#     pass

# if __name__ == "__main__":
#     filename  = sys.argv[1]
#     word = sys.argv[2]
#     with open(filename) as f:
#         string = f.read()
#         n = search_word(word, string)
#         print(n)



