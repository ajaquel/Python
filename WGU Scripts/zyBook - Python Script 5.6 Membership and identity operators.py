# Use the "in" operator
barcelona_fc_roster = ['Alves', 'Messi', 'Fabregas']

name = input('Enter name to check: ')

if name in barcelona_fc_roster:
    print('Found', name, 'on the roster.')
else:
    print('Could not find', name, 'on the roster.')




# Use the "not in" operator
barcelona_fc_roster = ['Alves', 'Messi', 'Fabregas']

name = input('Enter name to check: ')

if name not in barcelona_fc_roster:
    print('Could not find', name, 'on the roster.')
else:
    print('Found', name, 'on the roster.')



request_str = 'GET index.html HTTP/1.1'

if '/1.1' in request_str:
    print('HTTP protocol 1.1')

if 'HTTPS' not in request_str:
    print('Unsecured connection')



my_dict = {'A': 1, 'B': 2, 'C': 3}

if 'B' in my_dict:
    print("Found 'B'")
else:
   print("'B' not found")

# Membership operator does not check values
if 3 in my_dict:
    print('Found 3')
else:
    print('3 not found')



x = 500 + 500  # Create a new object with value 1000
y = 500 + 500  # Create a second object with value 1000
z = x  # Bind z to the same object as x

if z is x:
    print('z and x are bound to the same object,')
if z is not y:
    print('but z and y are not.')



special_list = [-99, 0, 44]
special_num = 17

if special_num in special_list:
    print('Special number')
else:
    print('Not special number')






