# Contents of my_funcs.py.
def factorial(num):
    """Calculates and returns the factorial (num!)"""
    x = 1
    for i in range(1, num + 1):
        x *= i

    return x




# Using factorial from my_funcs.py.
import my_funcs

n = int(input('Enter number: '))
fact = my_funcs.factorial(n)

for i in range(1, n + 1):
    print(i, end=' ')
    if i != n:
        print('*', end=' ')

print('=', fact)






# Basic usage of imported modules.
# Consider a file shapes.py with the following contents:

cr = '#'

def draw_square(size):
    for h in range(size):
        for w in range(size):
            print(cr, end='')
        print()

def draw_rect(height, width):
    for h in range(height):
        for w in range(width):
            print(cr, end='')
        print()

