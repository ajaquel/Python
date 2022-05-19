Tasks

WGU is providing additional practice exercises for all students. The best method of learning Python is to practice. This will also help you prepare for the assessment, which requires you to write code.

Note: PyFiddle version 3 or higher is highly recommended for these exercises. This ensures cross-platform compatibility and removes potential file system risks from bad code.

Below is a sample exercise. You should copy the entire code snippet into your Python editor. Your code should be placed in the area that says "student code goes here" highlighted in yellow. This is inside the function. When you run this entire code snippet, there are test cases below your code. Your output should match the expected output.

# Complete the function to print the first X number of characters in the given string
def printFirst(mystring, x):
# Student code goes here

# expected output: WGU
printFirst('WGU College of IT', 3)

# expected output: WGU College
printFirst('WGU College of IT', 11)
Task 1

Complete the function to return the directory name only from the given file name

import os

# Complete the function to return the current working directory
def getCurrentDirectory():
# Student code goes here

# expected output: /tmp
# if using PyFiddle.io otherwise it varies
print(getCurrentDirectory())
Task 2

Complete the function to return the directory name only from the given file name

import os

# Complete the function to return the directory name only from the given file name
def getDirectoryName(fileName):
# Student code goes here

# expected output: /var/www
print(getDirectoryName("/var/www/test.html"))

# expected output: /var/www/apple
print(getDirectoryName("/var/www/apple/test.html"))
Task 3

Complete the function to return the file name part only from the given file name

import os

# Complete the function to return the file name part only from the given file name
def getFileName(fileName):
# Student code goes here

# expected output: test.html
print(getFileName("/var/www/test.html"))

# expected output: names.txt
print(getFileName("/var/www/apple/names.txt"))
Task 4

Complete the function to return the directory name only from the given file name

import os

# Complete the function to create the specified file and return the file name
def createFile(filename):
# Student code goes here

# expected output: True
createFile("test.txt")
print(os.path.exists("test.txt"))
Task 5

Complete the function to print all files in the given directory

import os

# Complete the function to print all files in the given directory
def printFiles(someDirectory):
# Student code goes here

# expected output: main.py
# if using PyFiddle.io otherwise it varies
printFiles(os.getcwd())
Task 6

Complete the function to return FILE if the given path is a file or return DIRECTORY if the given path is a directory or return NEITHER is it's not a file or directory

import os

# Complete the function to return FILE if the given path is a file
# or return DIRECTORY if the given path is a directory
# or return NEITHER is it's not a file or directory
def whatIsIt(somePath):
# Student code goes here

# expected output: DIRECTORY
print(whatIsIt(os.getcwd()))

# expected output: FILE
print(whatIsIt(os.listdir(os.getcwd())[0]))

# expected output: NEITHER
print(whatIsIt('apple.pie.123.txt'))
Task 7

Complete the function to read the contents of the specified file and print the contents

import os

# Complete the function to read the contents of the specified file and print the contents
def printFileContents(filename):
# Student code goes here

# expected output: Hello
with open("test.txt", 'w') as f:
f.write("Hello")
printFileContents("test.txt")
Task 8

Complete the function to append the given new data to the specified file then print the contents of the file

import os

# Complete the function to append the given new data to the specified file then print the contents of the file
def appendAndPrint(filename, newData):
# Student code goes here

# expected output: Hello World
with open("test.txt", 'w') as f:
f.write("Hello ")
appendAndPrint("test.txt", "World")



