for variable in container:
    # Loop body: Sub-statements to execute
    # for each item in the container
# Statements to execute after the for loop is complete



channels = {
    'MTV': 35,
    'CNN': 28,
    'FOX': 11,
    'NBC': 4,
    'CBS': 12
}

for c in channels:
    print('%s is on channel %d' % (c, channels[c]))



#Using a for loop to access each character of a string.
my_str = ''
for character in "Take me to the moon.":
    my_str += character + '_'
print(my_str)





#For loop example: Calculating shop revenue.
daily_revenues = [
    2356.23,  # Monday
    1800.12,  # Tuesday
    1792.50,  # Wednesday
    2058.10,  # Thursday
    1988.00,  # Friday
    2002.99,  # Saturday
    1890.75   # Sunday
]

total = 0
for day in daily_revenues:
    total += day

average = total / len(daily_revenues)

print('Weekly revenue: $%f' % total)
print('Daily average revenue: $%f' % average)




names = [
    'Biffle',
    'Bowyer',
    'Busch',
    'Gordon',
    'Patrick'
]

for name in names:
    print(name, '|', end=' ')

print('\nPrinting in reverse:')
for name in reversed(names):
    print(name, '|', end=' ')





# Apple (APPL) stock prices 2005-2007
#$ 34.62
#$ 76.30
#$ 85.05

stock_prices = [34.62, 76.30, 85.05]
for price in stock_prices:
    print('$', price)





#Write a for loop to print each contact in contact_emails. Sample output for the given program:
#mike.filt@bmail.com is Mike Filt
#s.reyn@email.com is Sue Reyn
#narty042@nmail.com is Nate Arty

contact_emails = {
    'Sue Reyn' : 's.reyn@email.com',
    'Mike Filt': 'mike.filt@bmail.com',
    'Nate Arty': 'narty042@nmail.com'
}

for cont in contact_emails:
    print('%s is %s' % (contact_emails[cont], cont))




'''Program that calculates savings and interest'''

initial_savings = 10000
interest_rate = 0.05

years = int(input('Enter years: '))
print()

savings = initial_savings
for i in range(years):
    print(' Savings in year %d: $%f' % (i, savings))
    savings = savings + (savings*interest_rate)

print('\n')





'''Program that calculates savings and interest'''

initial_savings = 10000
interest_rate = 0.05

years = int(input('Enter years: '))
print()

savings = initial_savings
for i in range(0, years, 3):
    print(' Savings in year %d: $%f' % (i, savings))
    savings = savings + (savings*interest_rate*3)

print('\n')



