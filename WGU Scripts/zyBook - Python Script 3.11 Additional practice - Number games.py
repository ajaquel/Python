num = int(input('Enter 2 digit number:\n'))

result = num * (3*7*13*37)

print(result)


num = int(input('Enter 3 digit number:\n'))

result = num * (7*11*13)

print(result)


num = int(input('Enter 5 digit number:\n'))

result = num * (11*9091)

print(result)




# Complete the following program - NOT COMPLETED
# Times 11: A two-digit number can be easily multiplied by 11 in one's head
# simply by adding the digits and inserting that sum between the digits.
# For example, 43 * 11 has the resulting digits of 4, 4+3, and 3, yielding 473.
# If the sum between the digits is greater than 9, then the 1 is carried to the
# hundreds place. Complete the below program.


num_in_tens = int(input('Enter the tens digit:\n'))
num_in_ones = int(input('Enter the ones digit:\n'))

num_in = num_in_tens * 10 + num_in_ones

print('You entered', num_in)
print(num_in, '* 11 is', num_in * 11)

num_out_hundreds = num_in_tens
#num_out_tens = ?   FINISH
#num_out_ones = ?  FINISH

print('An easy mental way to find the answer is:')
print(num_in_tens, ',', num_in_tens, '+', num_in_ones, ',', num_in_ones)

#Build num_out from its digits:
#num_out = ? + ? + ?   FINISH

# Note this line will generate an error until the above program is complete.
print(num_out)
