# Multi-dimensional lists.
my_list = [[10, 20], [30, 40]]
print('First nested list:', my_list[0])
print('Second nested list:', my_list[1])
print('Element 0 of first nested list:', my_list[0][0])



# Representing a tic-tac-toe board using nested lists.
tic_tac_toe = [
    ['X', 'O', 'X'],
    [' ', 'X', ' '],
    ['O', 'O', 'X']
]

print(tic_tac_toe[0][0], tic_tac_toe[0][1], tic_tac_toe[0][2])
print(tic_tac_toe[1][0], tic_tac_toe[1][1], tic_tac_toe[1][2])
print(tic_tac_toe[2][0], tic_tac_toe[2][1], tic_tac_toe[2][2])




# The following example illustrates the use of a two-dimensional
# list in a distance between cities example.
#
# Run the following program, entering the text '1 2' as input
# to find the distance between LA and Chicago. Try other pairs.
# Next, try modifying the program by adding a new city, Anchorage,
# that is 3400, 3571, and 4551 miles from Los Angeles, Chicago,
# and Boston, respectively.
#
# Note that the styling of the nested list in this example makes
# use of indentation to clearly indicate the elements of each
# list -- the spacing does not affect how the interpreter
# evaluates the list contents.

# direct driving distances between cities, in miles
# 0: Boston    1: Chicago    2: Los Angeles

distances = [
    [
        0,
        960,  # Boston-Chicago
        2960 # Boston-Los Angeles
    ],
    [
        960,  # Chicago-Boston
        0,
        2011  # Chicago-Los Angeles
    ],
    [
        2960,  # Los Angeles-Boston
        2011,  # Los-Angeles-Chicago
        0
    ]
]

user_input = input('Enter city pair (Ex: 1 2) -- ').strip()
city1, city2 = user_input.split()

print('Distance: %d miles' % distances[int(city1)][int(city2)])




# A three-dimensional list structure as follows
nested_table = [
    [
        [10, 0, 55],
        [0, 4, 16]
    ],
    [
        [0, 0, 1],
        [1, 20, 2]
    ]
]





# Iterating over multi-dimensional lists.
currency = [
        [1.00, 5.00, 10.0], # US Dollars
        [0.75, 3.77, 7.53], # Euros
        [0.65, 3.25, 6.50]  # British pounds
]

for row in currency:
    for cell in row:
        print(cell, end=' ')
    print()




# Iterating through multi-dimensional lists using enumerate().
currency = [
   [1, 5, 10 ],  # US Dollars
   [0.75, 3.77, 7.53],  #Euros
   [0.65, 3.25, 6.50]  # British pounds
]
for row_index, row in enumerate(currency):
   for column_index, item in enumerate(row):
       print('currency[%d][%d] is %.2f' % (row_index, column_index, item))





# Other examples
nums = [
    [0, 2, 4, 6],
    [0, 3, 6, 9, 12]
]

for n1 in nums:
    for n2 in n1:
        print(n2, end=' ')
    print()





tictactoe = [
    ['X', 'O', 'O'],
    ['O', 'O', 'X'],
    ['X', 'X', 'X']
]

# Check for 3 Xs in one row
# (Doesn't check columns or diagonals)
for row in tictactoe:
    num_X_in_row = 0
    for square in row:
        if square == 'X':
            num_X_in_row += 1
    if num_X_in_row == 3:
        print('X wins!')
        break
else:
    print("Cat's game!")




# Print the two-dimensional list mult_table by row and column. Hint: Use nested loops. Sample output for the given program:
# 1 | 2 | 3
# 2 | 4 | 6
# 3 | 6 | 9
mult_table = [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]
for row, nums in enumerate(mult_table):
    for column, num in enumerate(nums):
          print(num, end='')
          if column == len(mult_table)-1:
                print()
          else:
                print(' |', end = ' ')


