# Conversion operators.
'string literal with conversion specifiers'  % (values_tuple)


# String formatting example: Add leading 0s by setting the minimum field width and 0 conversion flag.
student_id = int(input('Enter student ID: '))

print('The user entered %d' % student_id)
print('Full 8-character student ID: %08d' % student_id)




#String formatting example: Setting precision of floating-point values.
import math
real_pi = math.pi  # math library provides close approximation of pi
approximate_pi = 22.0 / 7.0  # Approximate pi to 2 decimal places

print('pi is %f.' % real_pi)
print('22/7 is %f.' % approximate_pi)
print('22/7 is accurate for 2 decimal places: %.2f' % approximate_pi)





#Complete the program to print out nicely formatted football player statistics.
# Match the following output as closely as possible -- the ordering of players
# is not important for this example.
'''
2012 quarterback statistics:
  Passes completed:
    Greg McElroy   :  19
    Aaron Rodgers  : 371
    Peyton Manning : 400
    Matt Leinart   :  16
  Passing yards:
    ...
  Touchdowns / Interception ratio:
    Greg McElroy   : 1.00
    Aaron Rodgers  : 4.88
    Peyton Manning : 3.36
    Matt Leinart   : 0.00
'''




quarterback_stats = {
    'Aaron Rodgers': {'COMP': 371, 'YDS': 4925, 'TD': 39, 'INT': 8},
    'Peyton Manning': {'COMP': 400, 'YDS': 4659, 'TD': 37, 'INT': 11},
    'Greg McElroy': {'COMP': 19, 'YDS': 214, 'TD': 1, 'INT': 1},
    'Matt Leinart': {'COMP': 16, 'YDS': 115, 'TD': 0, 'INT': 1}
}

print('2012 quarterback statistics:')

print('  Passes completed:')
for qb in quarterback_stats:
    comp = quarterback_stats[qb]['COMP']
    #print('    %?: %?' % (qb, comp))  # Replace conversion specifiers
    # Hint: Use the conversion flag '-' to left-justify names

print('  Passing yards:')
for qb in quarterback_stats:
    print('    QB: yards')

print('  Touchdown / interception ratio:')
# ...
# Hint: Convert TD/INTs to float before calculating ratio






#Comparing conversion operations using tuples and dicts.
import time
gmt = time.gmtime()  # Get current Greenwich Mean Time

print('Time is: %02d/%02d/%04d  %02d:%02d %02d sec' % \
      (gmt.tm_mon, gmt.tm_mday, gmt.tm_year, gmt.tm_hour, gmt.tm_min, gmt.tm_sec))

'''Time is: 06/07/2013  20:16 24 sec
...
Time is: 06/07/2013  20:16 28 sec
'''


import time
gmt = time.gmtime()  # Get current Greenwich Mean Time


print('Time is: %(month)02d/%(day)02d/%(year)04d  %(hour)02d:%(min)02d %(sec)02d sec' %  \
      {
        'year': gmt.tm_year, 'month': gmt.tm_mon, 'day': gmt.tm_mday,
        'hour': gmt.tm_hour, 'min': gmt.tm_min, 'sec': gmt.tm_sec
      }
)

'''
Time is: 06/07/2013  20:16 24 sec
...
Time is: 06/07/2013  20:16 28 sec
'''





#Print air_temperature with 1 decimal point followed by C. Sample output from given program:
# 36.4C

air_temperature = 36.4158102

''' Your solution goes here '''



