#Example using expressions: Minutes to hours/minutes.
# The program below reads in the number of minutes entered by a user.
# The program then converts the number of minutes to hours and minutes.
# Run the program, then modify the code to work in reverse: The user enters
# two numbers for hours and minutes and the program outputs total minutes.


minutes = int(input('Enter minutes:\n'))
hours = minutes // 60
minutes_remaining = minutes % 60

print(minutes, 'minutes is', end=' ')
print(hours, 'hours and', end=' ')
print(minutes_remaining, 'minutes.\n', end=' ')






#minutes = int(input('Enter minutes:\n'))
aj_hours = int(input('Enter hours:'))
aj_mins = int(input('Enter mins:'))

tot_mins = ((aj_hours * 60) + aj_mins)

#hours = minutes // 60
#minutes_remaining = minutes % 60

#print(minutes, 'minutes is', end=' ')
#print(hours, 'hours and', end=' ')
#print(minutes_remaining, 'minutes.\n', end=' ')
print(tot_mins)




user_val = 927
ones_digit     = user_val % 10    # Ex: 927 % 10 is 7.
tmp_val        = user_val // 10

tens_digit     = tmp_val % 10     # Ex: tmp_val = 927 // 10 is 92. Then 92 % 10 is 2.
tmp_val        = tmp_val // 10

hundreds_digit = tmp_val % 10     # Ex: tmp_val = 92 // 10 = 9. Then 9 % 10 is 9.





#Given a 10-digit phone number stored as an integer, % and / can be used to get any part,
#such as the prefix. For phone_num = 9365551212 (whose prefix is 555):

phone_num = int(input())
tmp_val = phone_num // 10000  # // 10000 shifts right by 4, so 936555.
prefix_num = tmp_val % 1000 # % 1000 gets the right 3 digits, so 555.
print(prefix_num)

#Dividing by a power of 10 shifts a value right. 321 // 10 is 32. 321 // 100 is 3.
# % by a power of 10 gets the rightmost digits. 321 % 10 is 1. 321 % 100 is 21.




#A cashier distributes change using the maximum number of five-dollar bills,
# followed by one-dollar bills. Ex: 19 yields 3 fives and 4 ones. Write a single
# statement that assigns num_ones with the number of distributed one-dollar bills
# given amount_to_change. Hint: Use %.

amount_to_change = 19
num_fives = amount_to_change // 5

num_ones = amount_to_change % 5

print('Change for $', amount_to_change)
print(num_fives, 'five dollar bill(s) and', num_ones, 'one dollar bill(s)')

