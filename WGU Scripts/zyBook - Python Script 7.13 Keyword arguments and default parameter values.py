# A function with many arguments.
def print_book_description(title, author, publisher, year, version, num_chapters, num_pages):
    # Format and print description of a book...

print_book_description('The Lord of the Rings', 'J. R. R. Tolkien', 'George Allen & Unwin',
                       1954, 1.0, 22, 456)



#Using keyword arguments.
def print_book_description(title, author, publisher, year, version, num_chapters, num_pages):
    # Format and print description of a book...

print_book_description(title='The Lord of the Rings', publisher='George Allen & Unwin',
                       year=1954, author='J. R. R. Tolkien', version=1.0,
                       num_pages=456, num_chapters=22)




# All keyword arguments must follow positional arguments.
def split_check(amount, num_people, tax_rate, tip_rate):
    # ...

split_check(125.00, tip_rate=0.15, num_people=2, tax_rate=0.095)




#Parameter with a default value.
def print_date(day, month, year, style=0):
    if style == 0:  # American
        print(month, '/', day, '/', year)
    elif style == 1:  # European
        print(day, '/', month, '/', year)
    else:
        print('Invalid Style')

print_date(30, 7, 2012, 0)
print_date(30, 7, 2012, 1)
print_date(30, 7, 2012)




#Valid function calls with default parameter values.
def print_date(day=1, month=1, year=2000, style=0)

print_date(30, 7, 2012, 0)   # Defaults: none
print_date(30, 7, 2012)      # Defaults:                            style=0
print_date(30, 7)            # Defaults:                 year=2000, style=0
print_date(30)               # Defaults:        month=1, year=2000, style=0
print_date()                 # Defaults: day=1, month=1, year=2000, style=0




#A common error is to provide a mutable object as a default parameter. For example,
# the statement modify_points(points=[]) provides a default empty list if the points
# argument is not specified. Such a definition is problematic because the default
# argument object is created once, at the time the function is defined. Thus, if
# the function modifies the default object when called, the default object will
# still be modified in future calls to that function. The below program demonstrates
# the problem with mutable default objects and illustrates a solution that creates a
# new empty list each time the function is called.
def my_func(value, my_list=[]):
    my_list.append(value)
    return my_list

numbers = my_func(50)  # default list appended with 50
print(numbers)
numbers = my_func(100)  # default list appended with 100
print(numbers)


#The left program shows a function my_func() that has an empty list as default value
# of my_list. A programmer might expect that each time the function is called without
# specifying my_list, a new empty list will be created and the result of the function
# will be [value]. However, the default object will instead maintain all appended
# elements across function calls. The solution replaces the default list with the
# None keyword, checking for that value and creating a new empty list in the local
# scope if necessary.
def my_func(value, my_list=None):
    if my_list == None:
        my_list = []
    my_list.append(value)
    return my_list

numbers = my_func(50)  # default list appended with 50
print(numbers)
numbers = my_func(100)  # default list appended with 100
print(numbers)




# Mixing keyword arguments and default parameter values allows omitting arbitrary arguments.
def print_date(day=1, month=1, year=2000, style=0):
    # ...


print_date(day=30, year=2012)   # Defaults:        month=1,            style=0
print_date(style=1)             # Defaults: day=1, month=1, year=2000
print_date(year=2012, month=4)  # Defaults: day=1,                     style=0





#Finish the split_check function. The split_check function should return the amount
# each diner must pay to cover the cost of the meal. Use default arguments to set
# tip_rate to 15% and tax_rate to 9% if the user does not specify them.
def split_check(check_amount, num_diners, tip_rate=0.15, tax_rate = 0.09):
    pass
    # FIXME: Finish the function. HINT: Calculate bill total with tip and tax,
    # then divide by the number of diners.


total = float(input('Enter bill total:\n'))
people = int(input('Enter number of diners:\n'))

print('Cost per diner:', split_check(total, people, tax_rate = 0.075))



# Completed
def split_check(check_amount, num_diners, tip_rate=0.15, tax_rate = 0.09):
    pass
    # FIXME: Finish the function. HINT: Calculate bill total with tip and tax,
    # then divide by the number of diners.
    bill_tip = total * tip_rate
    print(bill_tip)
    bill_tax = total * tax_rate
    print(bill_tax)
    bill_total = total + bill_tip + bill_tax
    print(bill_total)
    bill_each = bill_total / people
    return bill_each


total = float(input('Enter bill total:\n'))
people = int(input('Enter number of diners:\n'))

print('Cost per diner:', split_check(total, people, tax_rate = 0.075))




#Write a function number_of_pennies() that returns the total number of
# pennies given a number of dollars and (optionally) a number of pennies.
# Ex: 5 dollars and 6 pennies returns 506.
def number_of_pennies(dollars, pennies=0):
    dol_to_pen = dollars * 100
    total_pennies = dol_to_pen + pennies
    return total_pennies


print(number_of_pennies(5, 6)) # Should print 506
print(number_of_pennies(4))    # Should print 400


