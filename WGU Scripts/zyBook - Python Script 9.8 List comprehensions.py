# List comprehension.
new_list = [expression for name in iterable]




# List comprehension example: A first look.
my_list = [10, 20, 30]
list_plus_5 = [(i + 5) for i in my_list]

print('New list contains:', list_plus_5)




# Conditional list comprehensions.
new_list = [expression for name in iterable if condition]





#Conditional list comprehension example: Filter out odd numbers.
# Get a list of integers from the user
numbers = [int(i) for i in input('Enter numbers:').split()]

#Filter out odd numbers
even_numbers = [i for i in numbers if (i % 2) == 0]
print('Even numbers only:', even_numbers)




