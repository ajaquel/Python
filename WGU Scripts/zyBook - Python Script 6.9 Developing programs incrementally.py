#First version echoes input phone number string.
user_input = input('Enter phone number: ')

index = 0
for character in user_input:
    print('Element %d is: %s' % (index, character))
    index += 1


#Second version echoes numbers, and has FIXME comment.
user_input = input('Enter phone number: ')
phone_number = ''

for character in user_input:
    if '0' <= character <= '9':
        phone_number += character
    else:
        #FIXME: Add elif branches for letters and hyphen
        phone_number += '?'

print('Numbers only: %s' % phone_number)


#Third version echoes hyphens too, and handles first three letters.
user_input = input('Enter phone number: ')
phone_number = ''

for character in user_input:
    if ('0' <= character <= '9') or (character == '-'):
        phone_number += character
    elif ('a' <= character <= 'c') or ('A' <= character <= 'C'):
        phone_number += '2'
    #FIXME: Add remaining elif branches
    else:
        phone_number += '?'

print('Numbers only: %s' % phone_number)


#Fourth and final version sample input/output.
Enter phone number (letters/- OK, no spaces): 1-555-HOLIDAY
Numbers only: 1-555-4654329
...
Enter phone number (letters/- OK, no spaces): 1-555-holiday
Numbers only: 1-555-4654329
...
Enter phone number (letters/- OK, no spaces): 999-9999
Numbers only: 999-9999
...
Enter phone number (letters/- OK, no spaces): 9876zywx%$#@
Numbers only: 98769999????


#Complete the phone number program.
user_input = input('Enter phone number:\n')
phone_number = ''

for character in user_input:
    if ('0' <= character <= '9') or (character == '-'):
        phone_number += character
    elif ('a' <= character <= 'c') or ('A' <= character <= 'C'):
        phone_number += '2'
    elif ('d' <= character <= 'f') or ('D' <= character <= 'F'):
        phone_number += '3'
    elif ('g' <= character <= 'i') or ('G' <= character <= 'I'):
        phone_number += '4'
    elif ('j' <= character <= 'l') or ('J' <= character <= 'L'):
        phone_number += '5'
    elif ('m' <= character <= 'o') or ('M' <= character <= 'O'):
        phone_number += '6'
    elif ('p' <= character <= 's') or ('P' <= character <= 'S'):
        phone_number += '7'
    elif ('t' <= character <= 'v') or ('T' <= character <= 'V'):
        phone_number += '8'
    elif ('w' <= character <= 'z') or ('W' <= character <= 'Z'):
        phone_number += '9'
    elif (character == '+'):
        phone_number += '0'
    else:
        phone_number += '?'

print('Numbers only: %s' % phone_number)

