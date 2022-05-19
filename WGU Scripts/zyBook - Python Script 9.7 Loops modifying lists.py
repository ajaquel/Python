# Modifying a list during iteration example.
my_list = [3.2, 5.0, 16.5, 12.25]

for i in range(len(my_list)):
    my_list[i] += 5




# Modifying a list during iteration example: Converting negative values to 0.

#Correct Example
user_input = input('Enter numbers: ')

tokens = user_input.split()

# Convert strings to integers
nums = []
for token in tokens:
    nums.append(int(token))

# Print each position and number
print()
for pos, val in enumerate(nums):
    print('%d: %d' % (pos, val))

# Change negative values to 0
for pos in range(len(nums)):
    if nums[pos] < 0:
        nums[pos] = 0

# Print new numbers
print('New numbers: ')
for num in nums:
    print(num, end=' ')




# Incorrect Example (does not modify it since it does not changes the item)
user_input = input('Enter numbers:')

tokens = user_input.split()

# Convert strings to integers
nums = []
for token in tokens:
    nums.append(int(token))

# Print each position and number
print()
for pos, val in enumerate(nums):
    print('%d: %d' % (pos, val))

# Change negative values to 0
for num in nums:
    if num < 0:
        num = 0  # Logic error: temp variable num set to 0
    #if nums[num] < 0:  <- CORRECTION
    #    nums[num] = 0  <- CORRECTION

# Print new numbers
print('New numbers: ')
for num in nums:
    print(num, end=' ')



# tmp is assigned the value 10.0. 10.0 is an even number,
# so tmp%2 is 0 and the branch executes. nums[pos] = tmp assigns nums[1] to 10.0.
nums = [10, 20, 30, 40, 50]

for pos, value in enumerate(nums):
    tmp = value / 2
    if (tmp % 2) == 0:
        nums[pos] = tmp



# For example, consider the following program that reads in two sets of numbers and
# attempts to find numbers in the first set that are not in the second set.
#
# Figure 9.7.3: Modifying lists while iterating: Incorrect program.

nums1 = []
nums2 = []

user_input = input('Enter first set of numbers: ')
tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
for pos, val in enumerate(tokens):
    nums1.append(int(val))
    print('%d: %s' % (pos, val))

user_input = input('Enter second set of numbers:')
tokens = user_input.split()

# Convert strings to integers
print()
for pos, val in enumerate(tokens):
    nums2.append(int(val))
    print('%d: %s' % (pos, val))

# Remove elements from nums1 if also in nums2
print()
for val in nums1:
    if val in nums2:
        print('Deleting %d' % val)
        nums1.remove(val)

# Print new numbers
print('\nNumbers only in first set:', end=' ')
for num in nums1:
    print(num, end=' ')




# Copy a list using [:].
for item in my_list[:]:
    # Loop statements.






nums1 = []
nums2 = []

user_input = input('Enter first set of numbers: ')
tokens = user_input.split()  # Split into separate strings

# Convert strings to integers
for pos, val in enumerate(tokens):
    nums1.append(int(val))
    print('%d: %s' % (pos, val))

user_input = input('Enter second set of numbers:')
tokens = user_input.split()

# Convert strings to integers
print()
for pos, val in enumerate(tokens):
    nums2.append(int(val))
    print('%d: %s' % (pos, val))

# Remove elements from nums1 if also in nums2
print()
for val in nums1:
    if val in nums2:
        print('Deleting %d' % val)
        nums1.remove(val)

# Print new numbers
print('\nNumbers only in first set:', end=' ')
for num in nums1:
    print(num, end=' ')


