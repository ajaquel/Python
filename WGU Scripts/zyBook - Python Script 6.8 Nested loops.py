"""
Program to print all 2-letter domain names.

Note that ord() and chr() convert between text and the ASCII or Unicode encoding:
-  ord('a') yields the encoded value of 'a', the number 97.
-  ord('a')+1 adds 1 to the encoded value of 'a', giving 98.
-  chr(ord('a')+1) converts 98 back into a letter, producing 'b'
"""
print('Two-letter domain names:')

letter1 = 'a'
letter2 = '?'
while letter1 <= 'z':  # Outer loop
    letter2 = 'a'
    while letter2 <= 'z':  # Inner loop
        print('%s%s.com' % (letter1, letter2))
        letter2 = chr(ord(letter2) + 1)
    letter1 = chr(ord(letter1) + 1)




#Modify the program to include two-character .com names, where the second character
# can be a letter or a number, e.g., a2.com. Hint: Add a second while loop nested in
# the outer loop, but following the first inner loop, that iterates through the numbers 0-9.

'''
Program to print all 2-letter domain names.
Note that ord() and chr() convert between text and ASCII/ Unicode encodings.
ord('a') is 97. ord('b') is 98, and so on. chr(99) is 'c', etc.
'''
print('Two-letter domain names:')

letter1 = 'a'
number1 = 0
while letter1 <= 'z':  # Outer loop
    while number1 <= 9:    # Inner loop 2
         print('%s%d.com' % (letter1, number1))
         number1 = number1 + 1
    letter1 = chr(ord(letter1) + 1)



#Here is a nested loop example that graphically depicts an integer's
#magnitude by using asterisks, creating what is commonly called a histogram:

num = 0
while num >= 0:
    num = int(input('Enter an integer (negative to quit):\n'))

    if num >= 0:
        print('Depicted graphically:')
        for i in range(num):
            print('*', end=' ')
        print('\n')

print('Goodbye.')




#Modify the program to print one asterisk per 5 units. So if the user enters 40, print 8 asterisks.
num = 0
while num >= 0:
    num = int(input('Enter an integer (negative to quit):\n'))

    if num >= 0:
        print('Depicted graphically:')
        for i in range(0, num, 5):
            print('*', end=' ')
        print('\n')

print('Goodbye.')




#Nested loops examples
for i in range(5):
    for j in range(10, 12):
        print('%d%d' % (i1, i2))


c1 = 'a'
while c1 < 'b':
    c2 = 'a'
    while c2 <= 'c':
        print('%s%s' % (c1, c2), end=' ')
        c2 = chr(ord(c2) + 1)
    c1 = chr(ord(c1) + 1)



i1 = 1
while i1 < 19:
    i2 = 3
    while i2 <= 9:
        print('%d%d' % (i1,i2), end=' ')
        i2 = i2 + 3
    i1 = i1 + 10





#Write nested loops to print a rectangle. Sample output for given program:
#* * *
#* * *
num_rows = 2
num_cols = 3

for i1 in range(num_rows):
    for i2 in range(num_cols):
        print('*', end=' ')
    print()



#Given num_rows and num_cols, print a list of all seats in a theater.
# Rows are numbered, columns lettered, as in 1A or 3E. Print a space after
# each seat, including after the last. Ex: num_rows = 2 and num_cols = 3 prints:
#1A 1B 1C 2A 2B 2C
num_rows = 2
num_cols = 3

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces

r = 1
while r <= num_rows and num_cols != 0:
    c = 'A'
    while c <= 'C':
        print('%s%s' % (r,c), end=' ')
        c = chr(ord(c) + 1)
    r = r + 1
print()



