# String Slicing
url = 'http://en.wikipedia.org/wiki/Turing'
domain = url[7:23]  # Read 'en.wikipedia.org' from url
print(domain)



# A slice creates a new object.
my_str = "The cat jumped the brown cow"
animal = my_str[4:7]
print('The animal is a %s' % animal)

my_str = 'The fox jumped the brown llama'
print('The animal is still a', animal)  # animal variable remains unchanged.




# Slicing example: omitting start, end positions.
usr_text = input('Enter a string:\n')

first_half = usr_text[:len(usr_text)//2]
last_half = usr_text[len(usr_text)//2:]

print('The first half of the string is "%s"' % first_half)
print('The second half of the string is "%s"' % last_half)



# Slice stride.
numbers = '0123456789'

print('All numbers: %s' % numbers[::])
print('Every other number: %s' % numbers[::2])
print('Every third number between 1 and 8: %s' % numbers[1:9:3])




# String formatting example: Setting precision of floating-point values.
import math
real_pi = math.pi  # math library provides close approximation of pi
approximate_pi = 22.0 / 7.0  # Approximate pi to 2 decimal places

print('pi is %f.' % real_pi)
print('22/7 is %f.' % approximate_pi)
print('22/7 is accurate for 2 decimal places: %.2f' % approximate_pi)







# Complete the program to print out nicely formatted football player statistics.
# Match the following output as closely as possible -- the ordering of players is
# not important for this example.
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
    print('    %-15s: %4s' % (qb, comp))  # Replace conversion specifiers
    # Hint: Use the conversion flag '-' to left-justify names

print('  Passing yards:')
for qb in quarterback_stats:
    yards = quarterback_stats[qb]['YDS']
    #print('    QB: yards')
    print('    %-15s: %4s' % (qb, yards))

print('  Touchdown / interception ratio:')
for qb in quarterback_stats:
    td = quarterback_stats[qb]['TD']
    int = quarterback_stats[qb]['INT']
    ti_ratio = float(td) / float(int)
    print('    %-15s: %.2f' % (qb, ti_ratio))
# Hint: Convert TD/INTs to float before calculating ratio




# Comparing conversion operations using tuples and dicts.
import time
gmt = time.gmtime()  # Get current Greenwich Mean Time

print('Time is: %02d/%02d/%04d  %02d:%02d %02d sec' % \
      (gmt.tm_mon, gmt.tm_mday, gmt.tm_year, gmt.tm_hour, gmt.tm_min, gmt.tm_sec))



import time
gmt = time.gmtime()  # Get current Greenwich Mean Time

print('Time is: %(month)02d/%(day)02d/%(year)04d  %(hour)02d:%(min)02d %(sec)02d sec' %  \
      {
        'year': gmt.tm_year, 'month': gmt.tm_mon, 'day': gmt.tm_mday,
        'hour': gmt.tm_hour, 'min': gmt.tm_min, 'sec': gmt.tm_sec
      }
)



# Print air_temperature with 1 decimal point followed by C. Sample output from given program:
# 36.4C

air_temperature = 36.4158102

print('%.1f%s' % (air_temperature,'C'))



