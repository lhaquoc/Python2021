# Reading Files
from sys import argv
script, filename = argv

# open file by file name
txt = open(filename)

print(f"Here's your file {filename}")  # print file name
print(txt.read())  # print content of file

print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())
