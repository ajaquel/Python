#5.2.1: If statement: Hotel discount.
hotel_rate = 155

user_age = int(input('Enter age: '))

if user_age > 65:
   hotel_rate = hotel_rate - 20

print('Your hotel rate:', hotel_rate)



#5.2.3: If-else statement: Car insurance.
user_age = int(input('Enter age: '))

if user_age < 25:
 insurance_price = 4800
else:
 insurance_price = 2200

print('Annual price: $%d' % insurance_price)


#5.2.5: Writing an if-else statement.

if user_age > 62:
   item_discount = 15
else:
   item_discount = 0



   if num_people > 10:
   group_size = 2 * group_size
else:
   group_size = 3 * group_size
   num_people = num_people - 1



if num_players > 11:
   team_size = 11
else:
   team_size = num_players
team_size = 2 * team_size




#5.2.2: Basic if-else expression.
user_age = 17
if user_age <= 18:
   print('18 or less')
else:
   print('Over 18')


#5.2.3: Basic if-else.
user_tickets = 0

if user_tickets < 5:
    num_tickets = 1
else:
    num_tickets = user_tickets



#Figure 5.2.1: Multi-branch if-else example: Anniversaries.
num_years = int(input('Enter number years married: '))

if num_years == 1:
   print('Your first year -- great!')
elif num_years == 10:
   print('A whole decade -- impressive.')
elif num_years == 25:
   print('Your silver anniversary -- enjoy.')
elif num_years == 50:
   print('Your golden anniversary -- amazing.')
else:
   print('Nothing special.')


#5.2.4: Multi-branch if-else statements: Print century.
year = 1776

if year >= 2101:
    print('Distant future')
elif year >= 2001:
    print('21st century')
elif year >= 1901:
    print('20th century')
else:
    print('Long ago')

