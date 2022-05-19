# Clean-up actions using finally.
nums = []
my_file = input('Enter file name: ')

try:
    print('Opening', my_file)
    rd_nums = open(my_file, 'r')  # Might cause IOError

    for line in rd_nums:
        nums.append(int(line))  # Might cause ValueError
except IOError:
    print('Could not find', my_file)
except ValueError:
    print('Could not read number from', my_file)
finally:
    print('Closing', my_file)
    rd_nums.close()
    print('Numbers found:', ' '.join([str(n) for n in nums]))






# Finally. Assume that the following function has been defined.
def divide(a, b):
    z = -1
    try:
        z = a / b
    except ZeroDivisionError:
        print('Cannot divide by zero')
    finally:
        print('Result is', z)




