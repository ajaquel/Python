#Function example: Determining fees given an item selling price for an auction website.
def ebay_fee(sell_price):
    """Returns the fees charged by ebay.com given the selling
    price of fixed-price books, movies, music, or video games.
    fee is $0.50 to list plus 13% of selling price up to $50.00,
    5% of amount from $50.01 to $1000.00, and
    2% for amount $1000.01 or more."""

    p50 = 0.13  # for amount $50 and lower
    p50_to_1000 = 0.05  # for $50.01-$1000
    p1000 = 0.02  # for $1000.01 and higher
    fee = 0.50  # fee to list item

    if sell_price <= 50:
        fee  = fee + (sell_price * p50)
    elif sell_price <= 1000:
        fee = fee + (50 * p50) + ((sell_price - 50) * p50_to_1000)
    else:
        fee = fee + (50 * p50) + ((1000 - 50) * p50_to_1000) + ((sell_price-1000) * p1000)

    return fee

selling_price = float(input('Enter item selling price (ex: 65.00): '))
print('Ebay fee: $', ebay_fee(selling_price))







#The problem below uses the function get_numbers() to read a number of integers from the user.
# Three unfinished functions are defined, which should print only certain types of numbers that
# the user entered. Complete the unfinished functions, adding loops and branches where necessary.
size = 5

def get_numbers(num):
    numbers = []
    user_input = input('Enter %s integers:\n' % num)

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers

def print_all_numbers(numbers):
    # Print numbers
    print('Numbers:')

def print_odd_numbers(numbers):
    # Print all odd numbers
    print('Odd numbers:')

def print_negative_numbers(numbers):
    # Print all negative numbers
    print('Negative numbers:')

nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)



#Completed
size = 5

def get_numbers(num):
    numbers = []
    user_input = input('Enter %s integers:\n' % num)

    i = 0
    for token in user_input.split():
        number = int(token)     # Convert string input into integer
        numbers.append(number)  # Add to numbers list

        print(i, number)
        i += 1

    return numbers

def print_all_numbers(numbers):
    print('Numbers:', end=' ')
    for n in numbers:
        if n >= 0:
            print(n, end=' ')
        else:
            print(n, end=' ')

def print_odd_numbers(numbers):
    print('\nOdd numbers:', end=' ')
    for n in numbers:
        if n % 2 == 1:
            print(n, end=' ')

def print_negative_numbers(numbers):
    print('\nNegative numbers:', end=' ')
    for n in numbers:
        if n < 0:
            print(n, end=' ')

nums = get_numbers(size)
print_all_numbers(nums)
print_odd_numbers(nums)
print_negative_numbers(nums)




#Define function print_popcorn_time() with parameter bag_ounces. If bag_ounces is
# less than 3, print "Too small". If greater than 10, print "Too large". Otherwise,
# compute and print 6 * bag_ounces followed by "seconds".
def print_popcorn_time(bag_ounces):
    if bag_ounces < 3:
        print('Too small')
    elif bag_ounces > 10:
        print('Too large')
    else:
        print(6 * bag_ounces, 'seconds')

print_popcorn_time(7)




#Write a function shampoo_instructions() with parameter num_cycles. If num_cycles
# is less than 1, print "Too few.". If more than 4, print "Too many.". Else, print "N :
# Lather and rinse." num_cycles times, where N is the cycle number, followed by "Done.".
def shampoo_instructions(num_cycles):
    if num_cycles < 1:
        print('Too few.')
    elif num_cycles > 4:
        print('Too many.')
    else:
        i = 0
        while i < num_cycles:
            i += 1
            print (i,": Lather and rinse.")
        print('Done.')
shampoo_instructions(2)


