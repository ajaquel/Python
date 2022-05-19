# Simple use of command line arguments.
import sys

name = sys.argv[1]
age = int(sys.argv[2])

print('Hello %s. ' % name)
print('%d is a great age.\n' % age)





# Checking for proper number of command-line arguments.
import sys

if len(sys.argv) != 3:
    print('Usage: python myprog.py name age\n')
    sys.exit(1)  # Exit the program, indicating an error with 1.

name = sys.argv[1]
age = int(sys.argv[2])

print('Hello %s. ' % name)
print('%d is a great age.\n' % age)




