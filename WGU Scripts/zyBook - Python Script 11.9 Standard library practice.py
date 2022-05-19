# Using time library to access current local time.
import time
localtime = time.asctime( time.localtime(time.time()) )
print( "Local current time is:", localtime )





# Selecting randomized items from a list.
from random import choices
items = [12,6,4,18,3,5,16]
selection = choices(items, k=2)
print(selection)





# Using datetime to access the current date.
import datetime
print(datetime.date.today())






# Calculating a future date.
import datetime
span = datetime.timedelta(days=7)
today = datetime.date.today()
futuredate = today + span
print("One week from now will be: {}".format(futuredate))





# Calculate area of a circle.
from math import pi, ceil
def calcArea(radius):
        area = pi * (radius**2)
        return ceil(area)
print(calcArea(7))
print(calcArea(3))





# Example of applying help to an object.
import math
help(math)





# Example of applying help to a specific library method.
import random
help(random.choices)




# Practice problems

Task 1

Complete the function that takes an integer as input and returns the factorial of that integer

from math import factorial

def calculate(x):
# Student code goes here

print(calculate(3)) #expected outcome: 6
print(calculate(9)) #expected outcome: 362880
Task 2

Complete the function that takes a list as input and returns a randomized item from that list

import random as r

def selection(x):
# Student code goes here

print(selection(['apple','banana','orange','grape']))
print(selection([7,5,3,9,12,4,8,10]))
Task 3

Complete the function that takes as input an integer for a number of days and prints the total number of seconds in that number of days

import datetime

def currentDate(x):
# Student code goes here

currentDate(4) #expected outcome: The total number of seconds is 345600.0.
currentDate(7) #expected outcome: The total number of seconds is 604800.0.
Task 4

Complete the function to return the current date

import datetime as dt

def currentDate():
# Student code goes here

print(currentDate()) #Expected outcome will vary, but should follow this format: The current date is 9-11-2018.
Task 5

Complete the function that takes an integer as input, multiplies by e, and returns result rounded up

from math import e,ceil

def mathCalculation(x):
# Student code goes here

#expected outcome: 9
print(mathCalculation(3))

#expected outcome: 25
print(mathCalculation(9))
Task 6

Complete the function to return the number of leap years in the list

import calendar

# Complete the function to return the number of leap years in the list
def countLeapYears(yearList):
# Student code goes here

# expected output: 2
print(countLeapYears([2001, 2018, 2020, 2090, 2233, 2176, 2200, 2982]))

# expected output: 4
print(countLeapYears([2001, 2018, 2020, 2092, 2204, 2176, 2200, 2982]))
Task 7

Complete the function to print the full name of the month using the calendar library

import calendar

# Complete the function to print the full name of the month using the calendar library
def printMonthName(monthNum):
# Student code goes here

# expected output: March
printMonthName(3)

# expected output: November
printMonthName(11)
Task 8

Complete the function to print the full name of the day of the week

import calendar, datetime

# Complete the function to print the full name of the day of the week
def printWeekdayName(year, month, day):
# Student code goes here

# expected output: Friday
printWeekdayName(2001, 8, 31)

# expected output: Monday
printWeekdayName(2018, 10, 1)
Task 9

Complete the following function to return a random number between 5 and 8 exclusive

import random

# Complete the following function to return a random number
# between 5 and 8 exclusive
def getRandom():
# Student code goes here

# expected output: You should only get 5s, 6s, and 7s
for i in range(10):
    print(getRandom())
Task 10

Complete the function to add 90 days to the given date and return the new date

import datetime

# Complete the function to add 90 days to the given date and return the new date
def add90Days(someDate):
# Student code goes here

# expected output: 2018-12-30
print(add90Days(datetime.date(2018, 10, 1)))

# expected output: 2015-05-12
print(add90Days(datetime.date(2015, 2, 11)))



