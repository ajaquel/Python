# Using command-line arguments to specify the name of an input file.
import sys
import os

if len(sys.argv) != 2:
    print('Usage: %s input_file' % (sys.argv[0]))
    sys.exit(1)  # 1 indicates error

print('Opening file %s.' % sys.argv[1])

if not os.path.exists(sys.argv[1]):  # Make sure file exists
    print('File does not exist.')
    sys.exit(1)  # 1 indicates error

f = open(sys.argv[1], 'r')

# Input files should contain two integers on separate lines

print('Reading two integers.')
num1 = int(f.readline())
num2 = int(f.readline())

print('Closing file %s' % sys.argv[1])
f.close()  # Done with the file, so close it

print('\nnum1: %d' % num1)
print('num2: %d' % num2)
print('num1 + num2: %d' % (num1 + num2))





