# Writing to a file.
f = open('myfile.txt', 'w')  # Open file
f.write('Example string:\n  test...')  # Write string
f.close()  # Close the file




# Numeric values must be converted to strings.
num1 = 5
num2 = 7.5
num3 = num1 + num2

f = open('myfile.txt', 'w')
f.write(str(num1))
f.write(' + ')
f.write(str(num2))
f.write(' = ')
f.write(str(num3))
f.close()




# Using flush() to force an output buffer to write to disk.
import os

# Open a file with default line-buffering.
f = open('myfile.txt', 'w')

# No newline character, so not written to disk immediately
f.write('Write me to a file, please!')

# Force output buffer to be written to disk
f.flush()
os.fsync(f.fileno())

# ...



