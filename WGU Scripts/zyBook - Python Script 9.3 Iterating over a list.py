# Iterating through a list.
for my_var in my_list:
    # Loop body statements go here






# Iterating through a list example: Finding the maximum even number.
# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input('Enter numbers:')

tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
nums = []
for token in tokens:
    nums.append(int(token))

# Print each position and number
print()  # Print a single newline
for index in range(len(nums)):
    value = nums[index]
    print('%d: %d' % (index, value))

# Determine maximum even number
max_num = None
for num in nums:
    if (max_num == None) and (num % 2 == 0):
        # First even number found
        max_num = num
    elif (max_num != None) and (num > max_num ) and (num % 2 == 0):
        # Larger even number found
        max_num = num

print('Max even #:', max_num)




# For computing the sum, the program initializes a variable sum to 0,
# then simply adds the current iteration's list element value to that sum.
# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input('Enter numbers: ')

tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
print()
nums = []
for pos, token in enumerate(tokens):
    nums.append(int(token))
    print('%d: %s' % (pos, token))

sum = 0
for num in nums:
    sum += num

print('Sum:', sum)




# Compute the average, as well as the sum. Hint: You don't actually
# have to change the loop, but rather change the printed value.
# Print each number that is greater than 21.
# User inputs string w/ numbers: '203 12 5 800 -10'
user_input = input('Enter numbers: ')

tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
print()
nums = []
for pos, token in enumerate(tokens):
    nums.append(int(token))
    print('%d: %s' % (pos, token))

sum = 0
for num in nums:
    sum += num
    if num > 21:
        print(num)

print('Sum:', sum)
print('Average:', sum/len(nums))





# Complete the following program using functions from the table above to find
# some statistics about basketball player Lebron James. The code below provides
# lists of various statistical categories for the years 2003-2013. Compute and
# print the following statistics:
#
# Total career points
# Average points per game
# Years of the highest and lowest scoring season
#Lebron James: Statistics for 2003/2004 - 2012/2013
games_played = [79, 80, 79, 78, 75, 81, 76, 79, 62, 76]
points = [1654, 2175, 2478, 2132, 2250, 2304, 2258, 2111, 1683, 2036]
assists = [460, 636, 814, 701, 771, 762, 773, 663, 502, 535]
rebounds = [432, 588, 556, 526, 592, 613, 554, 590, 492, 610]

# Print total points
print('Total Points:', sum(points))

# Print Average PPG
ave_ppg = sum(points)/len(points)
print('Average PPG:', ave_ppg)

# Print best scoring year
print('Best Scoring:', max(points))

# Print worst scoring year
print('Best Scoring:', min(points))




# Write a loop to populate user_guesses with num_guesses integers.
# Read integers using int(input()). Ex: If num_guesses is 3 and user
# enters 9 5 2, then user_guesses is [9, 5, 2].
num_guesses = 3
user_guesses = []

''' Your solution goes here '''

print(user_guesses)



#Completed
num_guesses = 3
user_guesses = []

guess = 0
while guess < num_guesses:
    num = int(input())
    user_guesses.append(num)
    guess += 1

print(user_guesses)





# Assign sum_extra with the total extra credit received given list test_grades.
# Full credit is 100, so anything over 100 is extra credit. For the given program,
# sum_extra is 8 because 1 + 0 + 7 + 0 is 8. Sample output for the given program:
test_grades = [101, 83, 107, 90]
sum_extra = -999 # Initialize 0 before your loop

''' Your solution goes here '''

print('Sum extra:', sum_extra)



# Completed
test_grades = [101, 83, 107, 90]
sum_extra = -999 # Initialize 0 before your loop

sum_extra = 0

for grade in test_grades:
    if grade > 100:
        credit_count = grade - 100
        sum_extra = sum_extra + credit_count

print('Sum extra:', sum_extra)




# Write a loop to print all elements in hourly_temperature.
# Separate elements with a -> surrounded by spaces. Sample
# output for the given program:
# 90 -> 92 -> 94 -> 95
# Note: 95 is followed by a space, then a newline.
hourly_temperature = [90, 92, 94, 95]

''' Your solution goes here '''



# Completed
hourly_temperature = [90, 92, 94, 95]
arrow = '->'
final_list = []
for temp1 in hourly_temperature:
    final_list.append(temp1)
    final_list.append(arrow)
final_list.pop()
for temp2 in final_list:
    print(temp2, end=' ')
print()




