#The following is an example of using a loop to compute a mathematical quantity.
# The program computes the greatest common divisor (GCD) among two user-entered
# integers num_a and num_b, using Euclid's algorithm: If num_a > num_b, set num_a to
# num_a - num_b, else set num_b to num_b - num_a. Repeat until num_a equals num_b, at
# which point num_a and num_b both equal the GCD.

num_a = int(input('Enter first positive integer: '))
print()

num_b = int(input('Enter second positive integer: '))
print()

while num_a != num_b:
    if num_a > num_b:
        num_a = num_a - num_b
    else:
        num_b = num_b - num_a

print('GCD is %d' % num_a)



"""
Each time through the while loop, the program will check if the user-entered 
string user_text is equal to the string literal "Goodbye". If the two strings 
are not equal, the while loop contents will execute. Within the while loop, the 
program obtains a random number between 0 and 2 by using the random library. 
The randint() function provides a new random number each time the function is 
called. The arguments to randint(), 0 and 2, provide the minimum and maximum 
values that the function may return. Using the number given by randint(), the 
program's elif statements branch to a particular response.
"""

'''
Program that has a conversation with the user.
Uses elif branching and a random number to mix up the program's responses.
'''
import random  # Import a library to generate random numbers

print('Tell me something about yourself.')
print('You can type \'bye\' at anytime to quit.\n')

user_text = input()

while user_text != 'bye':
    random_num = random.randint(0, 2)  # Gives a random number between 0 and 2
    if random_num == 0:
        print('\nPlease explain further.\n')
    elif random_num == 1:
        print("\nWhy do you say: '%s'?\n" % user_text)
    elif random_num == 2:
        print('\nWhat else can you share?\n')
    else:
        print('\nUh-oh, something went wrong. Try again.\n')

    user_text = input()

print('It was nice talking with you. Goodbye.\n')







'''
Outputs average of list of positive integers
List ends with 0 (sentinel)
Ex: 10 1 6 3 0  yields (10 + 1 + 6 + 3) / 4, or 5
'''

values_sum = 0
num_values = 0

curr_value = int(input())

while curr_value > 0: # Get values until 0 (or less)
    values_sum += curr_value
    num_values += 1
    curr_value = int(input())

print('Average: %d\n' % (values_sum / num_values))







user_value = int(input())

maximum_value = user_value

while user_value > 0:
    if user_value > maximum_value:
        maximum_value = user_value
    user_value = int(input())

print('Max value:', maximum_value, end='')




#While loop with sentinel.
entered_age = int(input())

while (entered_age < 15 or entered_age > 30):
    if entered_age < 15:
        print('Too young')
    else:
         print('Already adult')
    entered_age = int(input())

print('Perfect fit', end='')





#Write an expression that continues to bid until the user enters 'n'.
import random
random.seed(5)

keep_going = '-'
next_bid = 0

while keep_going != 'n':
   next_bid = next_bid + random.randint(1, 10)
   print('I\'ll bid $%d!' % (next_bid))
   print('Continue bidding?', end=' ')
   keep_going = input()




#Given positive integer num_insects, write a while loop that prints that number doubled up to,
# but without exceeding 100. Follow each number with a space. Ex: If num_insects == 8, print: 8 16 32 64
num_insects = 8 # Must be >= 1

while (num_insects >= 0) and (num_insects <= 100):
        print(num_insects, end=' ')
        num_insects = num_insects * 2


