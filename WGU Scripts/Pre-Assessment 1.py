'''
def getlength(f_name, m_name, l_name):
    #Write your code in the white space here
    r1 = len(f_name)
    r2 = len(m_name)
    r3 = len(l_name)
    result = r1 + r2 + r3
    return result

getlength('Edward', 'Dale', 'Jonhson')


#Feedback
def getlength(f_name, m_name, l_name):
    return len(f_name + m_name + l_name)
getlength('Edward', 'Dale', 'Jonhson')

#----------------------------------------------------------



def getDate(day,month,date):
    #Write your code in the white space here
    print('Today is %s, %s %s' % (day, month, date))
    return


#Feedback
print("Today is " + day + ", " + month + " " + date + ".")

#----------------------------------------------------------


def slice_notation(nums):
#Write your code in the white space here
    list = nums
    sliced = list[5:8]
    print(sliced)
    return('')

slice_notation([1,2,3,4,5,6,7,8,9])


#Feedback
return nums[5:8]

#----------------------------------------------------------

def second_element (tup):
    #Write your code in the white space here
    list = tup
    print(list[1])
    return('')

second_element(['Python', 'Java', 2016, 2017])

#Feedback
return tup[1]

#----------------------------------------------------------

def getDimensions(dimensions):
    #Write your code in the white space here
    list = dimensions
    result = list[0] * list[1]
    print(result)
    return('')

getDimensions([50, 40])

#Feedback
length, width = dimensions
area=length*width
return area

#----------------------------------------------------------


def add_set(input1, input2 , input3):
    #Write your code in the white space here
    myset = set([input1, input2 , input3])
    print(myset)
    print(sorted(myset))
    return('')

add_set('German Shepard', 'Poodle' , 'Lab')


#Feedback
dogs = set()
dogs.add(input1)
dogs.add(input2)
dogs.add(input3)
return dogs

#----------------------------------------------------------


def get_grade(x):
    grades = {'Jerry': 85,'Emily': 96,'Tim': 76,'Grace': 84}
    #correct the following line of code to print the grade of x
    print(grades[x])

get_grade('Tim')


#Feedback
print(grades.get(x))

#----------------------------------------------------------


def top_two(input_list):
    #Write your code in the white space here
    list = input_list
    list1 = max(list)
    list.remove(max(list))
    list2 = max(list)
    result = list1, list2
    print(sorted(result))
    return('')

top_two([2,3,5,6,8,4,2,1])


#Feedback
return(sorted(input_list)[-2:])

#----------------------------------------------------------


def assessments2do(new_assessment, assessments_list):
    #Write code here to add new_assessment to assessment_list
    list = assessments_list
    list.append(new_assessment)
    print(list)
    return('')

assessments2do9(['Introduction to Python', 'Technical Communication'], [Scripting and Programming])


#Feedback
assessments_list.append(new_assessment)
return assessments_list

#----------------------------------------------------------


def multi(num1,num2,num3):
    #Write your code in the here
    result = num1 * num2 * num3
    print('The result of multiplying %d, %d, and %d is %d' % (num1, num2, num3, result))
    return('')

multi(4,5,6)


#Feedback
total=num1*num2*num3
return "The result of multiplying "+ str(num1)+", "+str(num2)+", and "+str(num3)+" is "+str(total)

#----------------------------------------------------------

import math
def nearest_square(number):
    #Write your code in the white space here
    result = math.sqrt(number)
    print(math.floor(result))
    return('')

nearest_square(18)


#Feedback
return (math.floor(math.sqrt(number)))

#----------------------------------------------------------


import os
def getdir():
    result = os.getcwd()
    print(result)
    return('')


#Feedback
print(os.getcwd())

#----------------------------------------------------------


def discard_number(my_set,number):
    #Write your code in the white space here
    myset = set(my_set)
    myset.remove(number)
    print(myset)
    return('')

discard_number((1, 3, 4, 5, 6), (4))


#Feedback
my_set.discard(number)
return my_set

#----------------------------------------------------------

from datetime import date
print(date.today())


#Feedback
from datetime import date
print date.today()

#----------------------------------------------------------

from     import random
randomNumber = random()
print(randomNumber)


#Feedback1
from random import random
randomNumber = random()
print randomNumber

#Feedback2
from random import *
randomNumber = random()
print randomNumber


#----------------------------------------------------------
import pandas as pd
data = {'name': ['Amy', 'Bob'],
'preTestScore': [4, 24],}
df = pd.DataFrame(data, columns = ['name', 'TestScore'])
df['TestScore'].describe()


'''


