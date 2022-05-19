curr_power = 2
user_char = 'y'

while user_char == 'y':
   print(curr_power)
   curr_power = curr_power * 2
   user_char = input()

print('Done')




nose = '0'  # Looks a little like a nose
user_value = '-'

while user_value != 'q':
    print(' {} {} '.format(user_value, user_value))  # Print eyes
    print('  {}  '.format(nose))  # Print nose
    print(user_value*5)  # Print mouth
    print('\n')

    # Get new character for eyes and mouth
    user_input = input("Enter a character ('q' for quit): \n")
    user_value = user_input[0]

print('Goodbye.\n')





...
# Read num from user ...

# Print each digit
while num > 0:
    print(num % 10)
    num = num // 10




year_considered = 2020  # Year being considered
num_ancestors = 2  # Approx. ancestors in considered year
years_per_generation = 20  # Approx. years per generation

user_year = int(input('Enter a past year (neg. for B.C.): '))
print()

while year_considered >= user_year:
    print('Ancestors in %d: %d' % (year_considered, num_ancestors))

    num_ancestors = num_ancestors * 2
    year_considered = year_considered - years_per_generation


user_num = 9;
while user_num >= 0:
  print('Body')
  user_num = int(input())

print('Done.')




#Write a while loop that prints user_num
# divided by 2 until user_num is less than 1. The value of user_num changes inside of the loop.
user_num = 20

while user_num >= 1:
    div_num = float(user_num / 2)
    print(div_num)
    user_num = div_num




