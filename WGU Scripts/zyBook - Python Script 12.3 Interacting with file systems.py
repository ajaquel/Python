# Using os.path.join() to create a portable file path string.
# The program below echoes the contents of logs stored in a
# hierarchical directory structure organized by date, using the
# os.path module to build a file path string that is portable
# across operating systems.

import os
import datetime

curr_day = datetime.date(1997, 8, 29)

num_days = 30
for i in range(num_days):
    year = str(curr_day.year)
    month = str(curr_day.month)
    day = str(curr_day.day)

    # Build path string using current OS path separator
    file_path = os.path.join('logs', year, month, day, 'log.txt')

    f = open(file_path, 'r')
    print('%s: %s' % (file_path, f.read()))
    f.close()

    curr_day = curr_day + datetime.timedelta(days=1)





# os.path.split(path) – Splits a path into a 2-tuple (head, tail),
# where tail is the last token in the path string and head is everything else.
import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
print(os.path.split(p))



# os.path.exists(path) – Returns True if path exists, else returns False.
import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
if os.path.exists(p):
    print('Suit up...')
else:
    print('The Lamborghini then?')



#os.path.isfile(path) – Returns True if path is an existing file, and false otherwise (e.g., path is a directory).
import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'bat_chopper')
if os.path.isfile(p):
    print('Found a file...')
else:
    print('Not a file...')



# os.path.getsize(path) – Returns the size in bytes of path.
import os
p = os.path.join('C:\\', 'Users', 'BWayne', 'batsuit.jpg')
print('Size of file:', os.path.getsize(p), 'bytes')





Directory structure organized by date.
logs/
    2009/
        April/
                1/
                 log.txt
                 words.doc
        January/
               15/
                 log.txt
               21/
                 log.txt
                 temp23.pdf
               24/
                 presentation.ppt
    2010/
        March/
             3/
              log.txt
             7/
              music.mp3




# Walking a directory tree.
import os

year = input('Enter year: ')
path = os.path.join('logs', year)
print()

for dirname, subdirs, files in os.walk(path):
    print(dirname, 'contains subdirectories:', subdirs, end=' ')
    print('and the files:', files)





# Filtering files using os.walk().
# Run the program and observe the above date-organized directory tree.
#
# Modify the program to print the contents of any file called log.txt in
# a given year's subdirectory, ignoring any other file.

import os

year = input('Enter year: ')
path = os.path.join('logs', year)
print()
for dirname, subdirs, files in os.walk(path):
    print(dirname, 'contains subdirectories:', subdirs, end=' ')
    print('and the files:', files)






