# Iterating N times using a loop variable
i = 1
while i <= N:
    # Loop body statements go here
    i = i + 1

i = 5
while i >= 1:
    # Loop body statements go here
    i = i - 1


i = 0
while i <= 100:
    # Loop body statements go here
    i = i + 2




#The following program outputs the amount of money in a savings account each year
# for the user-entered number of years, with $10,000 initial savings and 5% yearly interest:
'''Program that calculates savings and interest'''

initial_savings = 10000
interest_rate = 0.05

print('Initial savings of $%d' % initial_savings)
print('at %d%% yearly interest.\n' % (interest_rate*100))

years = int(input('Enter years: '))
print()

savings = initial_savings
i = 1  # Loop variable
while i <= years:  # Loop condition
    print(' Savings in year %d: $%f' % (i, savings))
    savings = savings + (savings*interest_rate)
    i = i + 1  # Increment loop variable

print('\n')




year = 1792
current_year = 2020

while year <= 2020:
    # Print the election year
    print(year)
    year = year + 4




#Write a program that lets a user enter N and that outputs N! (N factorial,
# meaning N*(N-1)*(N-2)*...*2*1). Hint: Initialize a variable total to N
# (where N is input), and use a loop variable i that counts from total-1
# down to 1. Compare your output with some of these
# answers: 1:1, 2:2, 3:6, 4:24, 5:120, 8:40320.
total = int(input())  # Read user-entered number

while i ? ??:
    # Set total to total * (i)
    # Decrement i

print(total)




i = 0
while i < N:
    # Loop body statements go here
    i += 1




i = 1
user_num = 4 # Assume positive

while i <= user_num:
    print(i)
    i += 1




num_stars = 3
num_printed = 0

while num_printed < num_stars:
    print('*')
    num_printed += 1


