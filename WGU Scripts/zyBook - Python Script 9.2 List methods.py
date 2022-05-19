# Complete the following program, as described above. Once finished, add the following commands:
#
# The rider can enter a name to find the current position in line. (Hint: Use the list.index() method.)
# The rider can enter a name to remove the rider from the line.

riders_per_ride = 3  # Num riders per ride to dispatch

line = []  # The line of riders
num_vips = 0  # Track number of VIPs at front of line

menu = ('(1) Reserve place in line.\n'  # Add rider to line
        '(2) Reserve place in VIP line.\n'  # Add VIP
        '(3) Dispatch riders.\n'  # Dispatch next ride car
        '(4) Print riders.\n'
        '(5) Exit.\n\n')

user_input = input(menu).strip().lower()

while user_input != '5':
    if user_input == '1':  # Add rider
        name = input('Enter name:').strip().lower()
        print(name)
        line.append(name)

    elif user_input == '2':  # Add VIP
        print(line.index(name)) #FIXME
        # Add new rider behind last VIP in line
        # Hint: Insert the VIP into the line at position num_vips.
        #Don't forget to increment num_vips.

    elif user_input == '3':  # Dispatch ride
        print(line.remove(name)) #FIXME
        # Remove last riders_per_ride from front of line.
        # Don't forget to decrease num_vips, if necessary.

    elif user_input == '4':  # Print riders waiting in line
        print('%d person(s) waiting:' % len(line), line)

    else:
        print('Unknown menu option')

    user_input = input('Enter command: ').strip().lower()
    print(user_input)




# Sort short_names in reverse alphabetic order. Sample output from given program:
# ['Tod', 'Sam', 'Joe', 'Jan', 'Ann']

short_names = ['Jan', 'Sam', 'Ann', 'Joe', 'Tod']
short_names.sort()
short_names.reverse()

print(short_names)


