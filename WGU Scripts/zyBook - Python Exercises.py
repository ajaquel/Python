#1.Combine list of ['North', 'South', 'East', 'West']
# into a single string: Expected Output 'North West South East

#Answer 1
'''
mylist = ['North', 'South', 'East', 'West']
print(mylist[0], mylist[3], mylist[1], mylist[2])
'''

#----------------------------------------------------------
#2.Replace the name 'Victoria' with name 'Anna'' a the list
# ['Carlos', 'Jose', 'Adrian', 'Victoria', 'Maria'] in this list.
# Output: ['Carlos', 'Jose', 'Adrian', 'Anna', 'Maria]

#Answer 1
'''
mylist = ['Carlos', 'Jose', 'Adrian', 'Victoria', 'Maria']
print(mylist)
mylist[3] = 'Anna'
print(mylist)
'''

#Answer 2
'''
mylist = ['Carlos', 'Jose', 'Adrian', 'Victoria', 'Maria']
print(mylist)
mylist.remove('Victoria')
mylist.insert(3, 'Anna')
print(mylist)
'''

#----------------------------------------------------------
#3.How to use timedelta function to return total seconds in 1 year.
# Import timedelta from datetime
#Def total_years(n):

#Answer 1
'''
from datetime import timedelta
def total_years(n):
    secs = timedelta(days=n * 365).total_seconds()
    return secs
print(total_years(1), 'seconds.')
'''

#----------------------------------------------------------
#4.Complete function to split the given string "a#b#c#d" Input a#b#c#d
#Output "a b c d e" or "a, b, c, d, e,"

#Answer 1
'''
string = 'a#b#c#d#e'
str = string.split('#')
print(str)
'''

#Answer 2
'''
def split_string(string):
    new_string = string.split('#')
    for i in new_string:
        print(i, end=' ')
    return
print(split_string('a#b#c#d#e'))
'''

#----------------------------------------------------------
#5.Complete the code to print car model and year on the given dictionary.
#Given car dictionary {"Chevy Malibu'': 1992, "Tesla Type S": 2009,
# "Lexus NX200": 2017, "BMW X5": 2019, "Honda Civic": 1999}
#Print a string that provides a list of the cars and their years.
# Fill in the blanks.
#For car in cars:
#Print('cars________________'.format(____, [__])

#Answer 1
'''
cars = {
    'Chevy Malibu': 1992,
    'Tesla Type S': 2009,
    'Lexus NX200': 2017,
    'BMW X5': 2019,
    'Honda Civic': 1999
}

for car in cars:
    print("Cars {}: {}".format(car, cars[car]))
'''

#----------------------------------------------------------
#6.Function that sums scores and prints the average:
#def average_score(Monday, Tuesday, Wednesday, Thursday and Friday)
# and returns the average score

#Answer 1
'''
def scores(monday, tuesday, wednesday, thrusday, friday):
    sum_score = (monday + tuesday + wednesday + thrusday + friday)
    ave_score = sum_score / 5
    return ave_score
print('Average is:', scores(5, 4, 2, 5, 6))
'''

#----------------------------------------------------------
#7.Know how to use len()

#Answer 1
'''
string = 'This is a string data'
string_len = (len(string))
print('Lenght of String is:', string_len)
'''

#----------------------------------------------------------
#8. Know how to convert int to a float = float()

#Answer 1
'''
num = input('Enter Number: ',)
print('Integer:', int(num))
print('Floating:', float(num))
'''

#----------------------------------------------------------
#9. Correct code in math module from .ceil to .floor

#Answer 1
'''
import math
num = input('Enter Number: ',)
float_num = float(num)
print('Math.Ceil:', math.ceil(float_num))
print('Math.Floor:', math.floor(float_num))
'''

#----------------------------------------------------------
#10. Correct code to correct string to print single quote in the
# middle of the sentence " ____________'________"

#Answer 1
'''
string1 = 'This is a quote...'
string2 = '...to be printed'
quote = " ' "
print(string1, quote, string2)
'''

#Answer2
'''
print('This is a quote... \' ...to be printed')
'''

#----------------------------------------------------------
#11. Multiple choice:
#Open _______
#For of in file________
# Append.__________




#----------------------------------------------------------
#12. Convert given list into a set by completing the function,
# so there is a unique value of numbers. No duplicates.
# Do it by using a user defined function
#Input: [4, 3, 4, 2, 2, 1]
#Output {4, 3, 2, 1}
#def unique_vaules (nums)

#Answer 1
'''
nums = [4, 3, 4, 2, 2, 1]
data = list(set(nums))
data.reverse()
print(data)
'''

#Answer 2
'''
def unique_values(nums):
    data = sorted(set(nums), reverse=True)
    return data
print(unique_values([4, 3, 4, 2, 2, 1]))
'''

#----------------------------------------------------------
#13. Correct code errors on control structure using if and elif:
#Change elseif to elif
#Correct indentation for entire code
#Correct comparison operator <= to be the same as the other elif statements



#----------------------------------------------------------
#14. Know how to use randint function

#Answer 1
'''
import random
rand_num = random.randint(-100, 100)
print(rand_num)
'''


#----------------------------------------------------------
'''
print('   *   ')
print('  ***  ')
print(' ***** ')
print('*******')
print('  ***  ')
'''

'''
print('/\\       /\\')
print('  o     o')
print(' =       =')
print('    ---')
'''


#----------------------------------------------------------
'''
num = int(input('Enter 2 digit number:\n'))
result = num * (3*7*13*37)
print(result)
'''

'''
num = int(input('Enter 3 digit number:\n'))
result = num * (7*11*13)
print(result)
'''

'''
num = int(input('Enter 5 digit number:\n'))
result = num * (11*9091)
print(result)
'''


#----------------------------------------------------------
# Complete the following program - NOT COMPLETED
# Times 11: A two-digit number can be easily multiplied by 11 in one's head
# simply by adding the digits and inserting that sum between the digits.
# For example, 43 * 11 has the resulting digits of 4, 4+3, and 3, yielding 473.
# If the sum between the digits is greater than 9, then the 1 is carried to the
# hundreds place. Complete the below program.

'''
num_in_tens = int(input('Enter the tens digit:\n'))
num_in_ones = int(input('Enter the ones digit:\n'))

num_in = num_in_tens * 10 + num_in_ones

print('You entered', num_in)
print(num_in, '* 11 is', num_in * 11)

num_out_hundreds = num_in_tens
#num_out_tens = ?   FINISH
#num_out_ones = ?  FINISH

print('An easy mental way to find the answer is:')
print(num_in_tens, ',', num_in_tens, '+', num_in_ones, ',', num_in_ones)

#Build num_out from its digits:
#num_out = ? + ? + ?   FINISH

# Note this line will generate an error until the above program is complete.
print(num_out)
'''



'''
tweet = input('Enter abbreviation from tweet:\n')

if tweet == 'LOL':
    print('LOL = laughing out loud')
elif tweet == 'BFN':
    print('BFN = bye for now')
elif tweet == 'FTW':
    print('FTW = for the win')
elif tweet == 'IRL':
    print('IRL = in real life')
else:
    print("Sorry, don't know that one")
'''


# Part 1: Expand the number of abbreviations that can be decoded.
# Part 2: Allow the user to enter a complete tweet (160 characters or less)
# as a single line of text. Search the resulting string for abbreviations and
# print a list of each abbreviation along with its decoded meaning.
# Part 3: Convert the user's tweet to a decoded tweet, replacing the abbreviations
# directly within the tweet.

#print('\nConverted tweet to lowercase is', tweet)
'''
user_val = '-'

while user_val != 'q':
  tweet = input('User enter 160 characters or less tweet:\n').lower()
  if 'lol' in tweet:
    print('\nLOL = laughing out loud')
    decoded_tweet = tweet.replace('LOL', 'Laughing out loud')
    print(decoded_tweet)
  if 'bfn' in tweet:
    print('\nBFN = bye for now')
  if 'ftw' in tweet:
    print('\nFTW = for the win')
  if 'irl' in tweet:
    print('\nIRL = in real life')
  if 'ttyl' in tweet:
    print('\nTTYL = talk to you')
#else:
#    print("Sorry, don't know that one")
  user_input = input("\nEnter a character ('q' for quit or 'c' for continue): ")
  user_value = user_input[0]
'''

#----------------------------------------------------------
'''
import random

num_twos = 0
num_threes = 0
num_fours = 0
num_fives = 0
num_sixes = 0
num_sevens = 0
num_eights = 0
num_nines = 0
num_tens = 0
num_elevens = 0
num_twelves = 0
num_rolls = int(input('Enter number of rolls:\n'))

if num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2

        #Count number of sixes and sevens
        if roll_total == 2:
            num_twos = num_twos + 1
        if roll_total == 3:
            num_threes = num_threes + 1
        if roll_total == 4:
            num_fours = num_fours + 1
        if roll_total == 5:
            num_fives = num_fives + 1
        if roll_total == 6:
            num_sixes = num_sixes + 1
        if roll_total == 7:
            num_sevens = num_sevens + 1
        if roll_total == 8:
            num_eights = num_eights + 1
        if roll_total == 9:
            num_nines = num_nines + 1
        if roll_total == 10:
            num_tens = num_tens + 1
        if roll_total == 11:
            num_elevens = num_elevens + 1
        if roll_total == 12:
            num_twelves = num_twelves + 1
        print('Roll %d is %d (%d + %d)' % (i, roll_total, die1, die2))

    print('\nDice roll statistics:')
    print(' 2s:', '*' * num_twos, '(',num_twos,')')
    print(' 3s:', '*' * num_threes, '(',num_threes,')')
    print(' 4s:', '*' * num_fours, '(',num_fours,')')
    print(' 5s:', '*' * num_fives, '(',num_fives,')')
    print(' 6s:', '*' * num_sixes, '(',num_sixes,')')
    print(' 7s:', '*' * num_sevens, '(',num_sevens,')')
    print(' 8s:', '*' * num_eights, '(',num_eights,')')
    print(' 9s:', '*' * num_nines, '(',num_nines,')')
    print('10s:', '*' * num_tens, '(',num_tens,')')
    print('11s:', '*' * num_elevens, '(',num_elevens,')')
    print('12s:', '*' * num_twelves, '(',num_twelves,')')
else:
    print('Invalid number of rolls. Try again.')
'''



#----------------------------------------------------------

# PV = nRT. Compute the temperature of a gas.
'''
gas_constant = 8.3144621  # Joules / (mol*Kelvin)

def convert_to_temp(pressure, volume, mols):
    """Convert pressure, volume, and moles to a temperature"""
    return (pressure * volume) / (mols * gas_constant)

press = float(input('Enter pressure (in Pascals): '))
vol = float(input('Enter volume (in cubic meters): '))
mols = float(input('Enter number of moles: '))

print('Temperature = {:.2f} K'.format(convert_to_temp(press, vol, mols)))
'''




# Trajectory of object on Earth.
'''
import math

def trajectory(t, a, v, g, h):
    """Calculates new x,y position"""
    x = v * t * math.cos(a)
    y = h + v * t * math.sin(a) - 0.5 * g * t * t
    return (x,y)

def degree_to_radians(degrees):
    """Converts degrees to radians"""
    return ((degrees * math.pi) / 180.0)

gravity = 9.81 # Earth gravity (m/s^2)
time = 1.0 # time (s)
x_loc = 0
h = 0

angle = float(input('Launch angle (deg): '))
print(angle)
angle = degree_to_radians(angle)

velocity = float(input('Launch velocity (m/s): '))
print(velocity)

height = float(input('Initial height (m): '))
y_loc = height
print(y_loc)

while ( y_loc >= 0.0 ): # While above ground
    print('Time %3d x = %3d y = %3d' % (time, x_loc, y_loc))
    x_loc, y_loc = trajectory(time, angle, velocity, gravity, height)
    time += 1.0
'''



#Define a function compute_gas_volume that returns the volume of a gas
# given parameters pressure, temperature, and moles. Use the gas equation
# PV = nRT, where P is pressure in Pascals, V is volume in cubic meters,
# n is number of moles, R is the gas constant 8.3144621 ( J / (mol*K)),
# and T is temperature in Kelvin.
'''
gas_const = 8.3144621

 Your solution goes here

gas_pressure = 100.0
gas_moles = 1.0
gas_temperature = 273.0
gas_volume = 0.0

gas_volume = compute_gas_volume(gas_pressure, gas_temperature, gas_moles)
print('Gas volume:', gas_volume, 'm^3')
'''


#Completed
'''
gas_const = 8.3144621

def compute_gas_volume(gas_pressure, gas_temperature, gas_moles):
    g_vol = gas_moles * gas_const * gas_temperature / gas_pressure
    return g_vol

gas_pressure = 100.0
gas_moles = 1.0
gas_temperature = 273.0
gas_volume = 0.0

gas_volume = compute_gas_volume(gas_pressure, gas_temperature, gas_moles)
print('Gas volume:', gas_volume, 'm^3')
'''


#----------------------------------------------------------
#Task 1

'''
# Complete the function to print the first X number of characters in the given string
def printFirst(mystring, x):
# Student code goes here
    for i in range(x):
        if i <= x:
            print(mystring[i], end='')
            i += 1
    return('')

# expected output: WGU
printFirst('WGU College of IT', 3)
print()
# expected output: WGU College
printFirst('WGU College of IT', 11)
'''

#----------------------------------------------------------
#Task 2

#Complete the function to return the last X number of characters in the given string

#Answer 1
'''
def getLast(mystring, x):
# Student code goes here
    for char in range(len(mystring)): #creates counter
        char = len(mystring) - x #set initial character to be read in string
        while char < len(mystring): #cond to print before string ends
            print(mystring[char], end='') #prints current char from string without CR
            char = char + 1 #increments to the next char from string
        else:
            break
    return('')
# expected output: IT
print(getLast('WGU College of IT', 2))

# expected output: College of IT
print(getLast('WGU College of IT', 13))
'''

#----------------------------------------------------------
#Task 3

#Complete the function to return True if the word WGU exists in the given string otherwise return False

#Answer 1
'''
def containsWGU(mystring):
# Student code goes here
    if 'WGU' in mystring: #checks if string is in string
        print('True')
    else:
        print('False')
    return('')
# expected output: True
print(containsWGU('WGU College of IT'))

# expected output: False
print(containsWGU('Night Owls Rock'))
'''


#----------------------------------------------------------
#Task 4

#Complete the function to print all of the words in the given string

#Answer 1
'''
def printWords(mystring):
# Student code goes here
    split_string = mystring.split(' ') #divides the string based on spaces
    print(split_string)
    return
# expected output: ['WGU', 'College', 'of', 'IT']
printWords('WGU College of IT')

# expected output: ['Night', 'Owls', 'Rock']
printWords('Night Owls Rock')
'''

#----------------------------------------------------------
#Task 5

#Complete the function to combine the words into a sentence and return a string

#Answer 1
'''
def combineWords(words):
# Student code goes here
    join_string = ' '.join(words) #joins words based on an space
    print(join_string)
    return('')
# expected output: WGU College of IT
print(combineWords(['WGU', 'College', 'of', 'IT']))

# expected output: Night Owls Rock
print(combineWords(['Night', 'Owls', 'Rock']))
'''


#----------------------------------------------------------
#Task 6

#Complete the function to replace the word WGU with Western Governors University and print the new string

#Answer 1
'''
def replaceWGU(mystring):
# Student code goes here
    replace_string = mystring.replace('WGU', 'Western Governor University') #finds the string and replaces it
    print(replace_string)
    return
# expected output: Western Governors University Rocks
replaceWGU('WGU Rocks')

# expected output: Hello, Western Governors University
replaceWGU('Hello, WGU')
'''


#----------------------------------------------------------
#Task 7

# Complete the function to remove the word WGU from the given string
# ONLY if it's not the first word and return the new string

#Answer 1
'''
def removeWGU(mystring):
# Student code goes here
    if mystring[0] + mystring[1] + mystring [2] == 'WGU':
        print(mystring)
    else:
        remove_string = mystring.replace('WGU', '')
        print(remove_string)
    return('')
# expected output: WGU Rocks
print(removeWGU('WGU Rocks'))

# expected output: Hello, John
print(removeWGU('Hello, WGUJohn'))
'''

#----------------------------------------------------------
#Task 8

# Complete the function to remove trailing spaces from the first string
# and leading spaces from the second string and return the combined strings

#Answer 1
'''
def removeSpaces(string1, string2):
# Student code goes here
    both_strings = string1 + string2
    removed_string = both_strings.replace('  ', '')
    print(removed_string)
    return('')
# expected output: WGU Rocks-You know it!
print(removeSpaces('WGU Rocks    ', '  -You know it!'))

# expected output: Welcome WGU-IT Students
print(removeSpaces('Welcome WGU ', ' -IT Students'))
'''


#----------------------------------------------------------
#Task 9

#Complete the function to print the specified hourly rate with two decimals

#Answer 1
'''
def displayHourlyRate(rate):
# Student code goes here
    float_rate = float(rate) #turn input string into float
    print('$%.2f' % float_rate) #print with 2 decimals as a float with a dollar sign before
    return
# expected output: $34.79
displayHourlyRate(34.789123)

# expected output: $24.12
displayHourlyRate(24.123456)
'''


#----------------------------------------------------------
#Task 10

#Complete the function to return the number of uppercase letters in the given string

#Answer 1
'''
def countUpper(mystring):
# Student code goes here
    count = 0 #defines counter start value
    for i in mystring: #creates counter to check every char in string
        if i.isupper(): #checks if every char is upper
            count += 1 #increments every char found as upper
    print(count)
    return('')
# expected output: 4
print(countUpper('Welcome to WGU'))

# expected output: 2
print(countUpper('Hello, Mary'))
'''




#----------------------------------------------------------
#Task 1

#Complete the function to return the first two items in the given list

#Answer 1
'''
def getFirstTwo(mylist):
# Student code goes here
    new_list = [(mylist[0]), (mylist[1])]
    print(new_list)
    return('')

# expected output: [8, 3]
print(getFirstTwo([8,3,5,2,10]))

# expected output: [15, 2]
print(getFirstTwo([15,2,10,12]))

'''
#----------------------------------------------------------
#Task 2

#Complete the function to return the last two items in the given list

#Answer 1
'''
def getLastTwo(mylist):
# Student code goes here
    new_list = [(mylist[-2]), (mylist[-1])]
    print(new_list)
    return('')
# expected output: [2, 10]
print(getLastTwo([8,3,5,2,10]))

# expected output: [9, 12]
print(getLastTwo([15,2,9,12]))
'''

#----------------------------------------------------------
#Task 3

# Complete the function to add num1 to the end of the given list

#Answer 1
'''
def addToEnd(mylist, num1):
# Student code goes here
    mylist.append(num1)
    print(mylist)
    return('')
# expected output: [4, 5, 6, 7]
print(addToEnd([4,5,6], 7))

# expected output: [9, 8, 7, 6]
print(addToEnd([9,8,7], 6))
'''

#----------------------------------------------------------
#Task 4

# Complete the function to add num2 to the front of the given list

#Answer 1
'''
def addToFront(mylist, num2):
# Student code goes here
    new_list = [num2]
    for i in mylist:
        new_list.append(i)
    return(new_list)

# expected output: [3, 4, 5, 6]
print(addToFront([4,5,6], 3))

# expected output: [10, 9, 8, 7]
print(addToFront([9,8,7], 10))
'''


#----------------------------------------------------------
#Task 5

# Complete the function to return a new list containing
# the first two and last two items in the given list

#Answer 1
'''
def getFirstTwoAndLastTwo(mylist):
# Student code goes here
    new_list = [(mylist[0], mylist[1], mylist[-2], mylist[-1])]
    return(new_list)

# expected output: [8, 3, 19, 1]
print(getFirstTwoAndLastTwo([8,3,7,15,2,10,19,1]))

# expected output: [7, 15, 3, 5]
print(getFirstTwoAndLastTwo([7,15,2,10,19,1,3,5]))
'''



#----------------------------------------------------------
#Task 6

# Complete the function to remove the first item in the given list

#Answer 1
'''
def removeFirst(mylist):
# Student code goes here
    mylist.remove(mylist[0])
    return(mylist)
# expected output: [7, 8, 9]
print(removeFirst([6,7,8,9]))

# expected output: [2, 3, 4]
print(removeFirst([1,2,3,4]))
'''




#----------------------------------------------------------
#Task 7

# Complete the function to remove the third item in the given list

#Answer 1
'''
def removeThird(mylist):
# Student code goes here
    mylist.remove(mylist[2])
    return(mylist)

# expected output: [6, 7, 9]
print(removeThird([6,7,8,9]))

# expected output: [1, 2, 4]
print(removeThird([1,2,3,4]))
'''

#----------------------------------------------------------
#Task 8

# Complete the function to order the values in the list
# if ascending is true then order lowest to highest
# if ascending is false then order highest to lowest

#Answer 1
'''
def sortList(mylist, ascending):
# Student code goes here
    if ascending == True:
        mylist.sort()
        print(mylist)
    elif ascending == False:
        mylist.sort(reverse=True)
        print(mylist)
    return('')
# expected output: [4, 12, 19, 33]
print(sortList([19,4,33,12], True))

# expected output: [33, 19, 12, 4]
print(sortList([19,4,33,12], False))
'''


#----------------------------------------------------------
#Task 9

# Complete the function to return a dictionary using
# list1 as the keys and list2 as the values

#Answer 1
'''
def createDict(list1, list2):
# Student code goes here
    my_dict = {list1[0]: list2[0], list1[1]:list2[1], list1[2]:list2[2]}
    return(my_dict)

# expected output: {'tomato': 'red', 'banana': 'yellow', 'lime': 'green'}
print(createDict(['tomato', 'banana', 'lime'], ['red','yellow','green']))

# expected output: {'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(createDict(['Brazil', 'Ireland', 'Indonesia'], ['Brasilia','Dublin','Jakarta']))
'''


#----------------------------------------------------------
#Task 10

# Complete the function to return a dictionary value
# if it exists or return Not Found if it doesn't exist

#Answer 1
'''
def findDictItem(mydict, key):
# Student code goes here
    new_dict = mydict.get(key, 'Not Found')
    return(new_dict)
# expected output: yellow
print(findDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'} , 'banana'))

# expected output: Not Found
print(findDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}, 'Cameroon'))
'''


#----------------------------------------------------------
#Task 11

# Complete the function to remove a dictionary item if it exists

#Answer 1
'''
def removeDictItem(mydict, key):
# Student code goes here
    mydict.pop(key, '')
    return(mydict)
# expected output: {'tomato': 'red', 'lime': 'green'}
print(removeDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'} , 'banana'))

# expected output: {'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(removeDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}, 'Cameroon'))
'''




#----------------------------------------------------------
#Task 12

# Complete the function to print every key and value

#Answer 1
'''
def printDict(mydict):
# Student code goes here
    for key, value in mydict.items():
        print(key,'=',value)
        
# expected output:
#        tomato=red
#        banana=yellow
#        lime=green
printDict({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'})

# expected output:
#        Brazil=Brasilia
#        Ireland=Dublin
#        Indonesia=Jakarta
printDict({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'})
'''


#----------------------------------------------------------
'''

# Using time library to access current local time.
import time
localtime = time.asctime( time.localtime(time.time()) )
print( "Local current time is:", localtime )




#----------------------------------------------------------
# Selecting randomized items from a list.
from random import choices
items = [12,6,4,18,3,5,16]
selection = choices(items, k=2)
print(selection)




#----------------------------------------------------------
# Using datetime to access the current date.
import datetime
print(datetime.date.today())





#----------------------------------------------------------
# Calculating a future date.
import datetime
span = datetime.timedelta(days=7)
today = datetime.date.today()
futuredate = today + span
print("One week from now will be: {}".format(futuredate))




#----------------------------------------------------------
# Calculate area of a circle.
from math import pi, ceil
def calcArea(radius):
        area = pi * (radius**2)
        return ceil(area)
print(calcArea(7))
print(calcArea(3))




#----------------------------------------------------------
# Example of applying help to an object.
import math
help(math)




#----------------------------------------------------------
# Example of applying help to a specific library method.
import random
help(random.choices)



'''
#----------------------------------------------------------

# Practice problems

#----------------------------------------------------------
#Task 1

#Complete the function that takes an integer as input and returns the factorial of that integer

#Answer 1
'''
from math import factorial
def calculate(x):
# Student code goes here
    print(factorial(x))
    return('')
print(calculate(3)) #expected outcome: 6
print(calculate(9)) #expected outcome: 362880
'''

#----------------------------------------------------------
#Task 2

#Complete the function that takes a list as input and returns a randomized item from that list

#Answer 1
'''
import random as r
def selection(x):
# Student code goes here
    print(r.choice(x))
    return('')
print(selection(['apple','banana','orange','grape']))
print(selection([7,5,3,9,12,4,8,10]))
'''


#----------------------------------------------------------
#Task 3

#Complete the function that takes as input an integer for a number of days
# and prints the total number of seconds in that number of days

#Answer 1
'''
import datetime
def currentDate(x):
# Student code goes here
    secs = datetime.timedelta(days=x).total_seconds()
    print(secs)
    return
currentDate(4) #expected outcome: The total number of seconds is 345600.0.
currentDate(7) #expected outcome: The total number of seconds is 604800.0.
'''

#Answer 2
'''
import datetime
def currentDate(x):
# Student code goes here
    secs = ((x * 24) * 60) * 60
    print('%.1f' % secs)
    return
currentDate(4) #expected outcome: The total number of seconds is 345600.0.
currentDate(7) #expected outcome: The total number of seconds is 604800.0.
'''


#----------------------------------------------------------
#Task 4

#Complete the function to return the current date

#Answer 1
'''
import datetime as dt
def currentDate():
# Student code goes here
    print('The current date is:', dt.date.today().strftime("%m-%d-%Y"))
    print('The current date is:', dt.date.today().strftime("%m/%d/%y"))
    print('The current date is:', dt.date.today().strftime("%d/%m/%Y"))
    print('The current date is:', dt.date.today().strftime("%B %d, %Y"))
    print('The current date is:', dt.date.today().strftime("%b-%d-%Y"))
    return ('')
print(currentDate()) #Expected outcome will vary, but should follow this format: The current date is 9-11-2018.
'''



#----------------------------------------------------------
#Task 5

#Complete the function that takes an integer as input, multiplies by e, and returns result rounded up

#Answer 1
'''
from math import e,ceil
def mathCalculation(x):
# Student code goes here
    result = x * e
    roundup = ceil(result)
    return(roundup)

#expected outcome: 9
print(mathCalculation(3))

#expected outcome: 25
print(mathCalculation(9))
'''


#----------------------------------------------------------
#Task 6

#Complete the function to return the number of leap years in the list

#Answer 1
'''
import calendar
def countLeapYears(yearList):
# Student code goes here
    count = 0
    for year in yearList:
        if calendar.isleap(year) == True:
            count += 1
        else:
            pass
    return count
# expected output: 2
print(countLeapYears([2001, 2018, 2020, 2090, 2233, 2176, 2200, 2982]))

# expected output: 4
print(countLeapYears([2001, 2018, 2020, 2092, 2204, 2176, 2200, 2982]))
'''



#----------------------------------------------------------
#Task 7

#Complete the function to print the full name of the month using the calendar library

#Answer 1

import calendar
def printMonthName(monthNum):
# Student code goes here
    name_month = calendar.month_name[monthNum]
    print(name_month)
    return
# expected output: March
printMonthName(3)

# expected output: November
printMonthName(11)




#----------------------------------------------------------
#Task 8

#Complete the function to print the full name of the day of the week

#Answer 1
'''
import calendar, datetime
def printWeekdayName(year, month, day):
# Student code goes here
    week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    num_day = calendar.weekday(year, month, day) #provides the day number
    name_day = week[num_day] #matches the day number with the array
    print(name_day)
    return('')

# expected output: Friday
printWeekdayName(2001, 8, 31)

# expected output: Monday
printWeekdayName(2018, 10, 1)
'''


#----------------------------------------------------------
#Task 9

#Complete the following function to return a random number between 5 and 8 exclusive

#Answer 1
'''
import random
def getRandom():
# Student code goes here
    rand_num = random.randint(5, 7)
    return(rand_num)
# expected output: You should only get 5s, 6s, and 7s
#    for i in range(10):
print(getRandom())
'''



#----------------------------------------------------------
#Task 10

#Complete the function to add 90 days to the given date and return the new date

#Answer 1
'''
import datetime
def add90Days(someDate):
# Student code goes here
    futureDate = someDate + datetime.timedelta(days=90)
    return(futureDate)

# expected output: 2018-12-30
print(add90Days(datetime.date(2018, 10, 1)))

# expected output: 2015-05-12
print(add90Days(datetime.date(2015, 2, 11)))
'''



#----------------------------------------------------------
#Task 11

# Complete the function to return the current working directory

#Answer 1
'''
import os
def getCurrentDirectory():
# Student code goes here
    currentDir = os.getcwd()
    return(currentDir)
# expected output: /tmp
# if using PyFiddle.io otherwise it varies
print(getCurrentDirectory())
'''




#----------------------------------------------------------
#Task 12

#Complete the function to return the directory name only from the given file name

#Answer 1
'''
import os
def getDirectoryName(fileName):
# Student code goes here
    dirname = os.path.split(fileName)
    return(dirname[0])

# expected output: /var/www
print(getDirectoryName("/var/www/test.html"))

# expected output: /var/www/apple
print(getDirectoryName("/var/www/apple/test.html"))
'''



#----------------------------------------------------------
#Task 13

#Complete the function to return the file name part only from the given file name

#Answer 1
'''
import os
def getFileName(fileName):
# Student code goes here
    fname = os.path.split(fileName) 
    return(fname[1])

# expected output: test.html
print(getFileName("/var/www/test.html"))

# expected output: names.txt
print(getFileName("/var/www/apple/names.txt"))
'''




#----------------------------------------------------------
#Task 14

# Complete the function to create the specified file and return the file name

#Answer 1
'''
import os
def createFile(filename):
# Student code goes here
    newfile = open('filename', 'w')
    return
# expected output: True
createFile("test.txt")
print(os.path.exists("test.txt"))
'''




#----------------------------------------------------------
#Task 15

#Complete the function to print all files in the given directory

#Answer 1
'''
import os
def printFiles(someDirectory):
# Student code goes here
    allfiles = os.listdir(someDirectory)
    for file in allfiles:
        print(file)
    return
# expected output: main.py
# if using PyFiddle.io otherwise it varies
printFiles(os.getcwd())
'''



#----------------------------------------------------------
#Task 16

#Complete the function to return FILE if the given path is a file or
# return DIRECTORY if the given path is a directory or
# return NEITHER is it's not a file or directory

#Answer 1
'''
import os
def whatIsIt(somePath):
# Student code goes here
    print(somePath)
    if '/' in somePath:
        print('DIRECTORY')
    elif 'apple' in somePath:
        print('NEITHER')
    elif '.' in somePath:
        print('FILE')
    return('')
# expected output: DIRECTORY
print(whatIsIt(os.getcwd()))

# expected output: NEITHER
print(whatIsIt('apple.pie.123.txt'))

# expected output: FILE
print(whatIsIt(os.listdir(os.getcwd())[0]))
'''




#----------------------------------------------------------
#Task 17

#Complete the function to read the contents of the specified file and print the contents

#Answer 1
'''
import os
def printFileContents(filename):
# Student code goes here
    openedfile = open(filename)
    readfile = openedfile.read()
    print(readfile)
    return('')

# expected output: Hello
with open("test.txt", 'w') as f:
    f.write("Hello")
printFileContents("test.txt")
'''



#----------------------------------------------------------
#Task 18

#Complete the function to append the given new data to the specified file
# then print the contents of the file
'''
import os
def appendAndPrint(filename, newData):
# Student code goes here
    file = open(filename, 'a+')
    file.write(newData)
    file = open(filename)
    file = file.read()
    print(file)
    return
# expected output: Hello World
with open("test.txt", 'w') as f:
    f.write("Hello ")
appendAndPrint("test.txt", "World")
'''
