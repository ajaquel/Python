# Creating a file object and reading text.
print('Opening file myfile.txt.')
f = open('myfile.txt')  # create file object

print('Reading file myfile.txt.')
contents = f.read()  # read file text into a string

print('Closing file myfile.txt.')
f.close()  # close the file

print('\nContents of myfile.txt:\n', contents)




# Calculating the average of data values stored in a file.
# The file "mydata.txt" contains 100 integers, each on its own line:

# Read file contents
print ('Reading in data...')
f = open('mydata.txt')
lines = f.readlines()
f.close()

# Iterate over each line
print('\nCalculating average...')
total = 0
for ln in lines:
    total += int(ln)

# Compute result
avg = total/len(lines)
print('Average value:', avg)





# Iterating over the lines of a file.
"""Echo the contents of a file."""
f = open('myfile.txt')

for line in f:
    print(line)

f.close()





