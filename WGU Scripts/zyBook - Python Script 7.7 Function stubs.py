#Using the pass statement in a function stub performs no operation.
def steps_to_feet(num_steps):
    feet_per_step = 3
    feet = num_steps * feet_per_step
    return feet

def steps_to_calories(num_steps):
    pass

steps = int(input('Enter number of steps walked: '))

feet = steps_to_feet(steps)
print('Feet:', feet)

calories = steps_to_calories(steps)
print('Calories:', calories)


# A function stub using a print statement.
def steps_to_calories(steps):
    print('FIXME: finish steps_to_calories')
    return -1



#Stopping the program using NotImplementedError in a function stub.
import math

def get_points(num_points):
    """Get num_points from the user. Return a list of (x,y) tuples."""
    raise NotImplementedError

def side_length(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def get_perimeter_length(points):
    perimeter = side_length(points[0], points[1])
    perimeter += side_length(points[0], points[2])
    perimeter += side_length(points[1], points[2])
    return perimeter

coordinates = get_points(3)
print('Perimeter of triangle:', get_perimeter_length(coordinates))





#Define stubs for the functions get_user_num() and compute_avg(). Each stub should print
# "FIXME: Finish function_name()" followed by a newline, and should return -1. Each stub
#  must also contain the function's parameters. Example output:
#FIXME: Finish get_user_num()
#FIXME: Finish get_user_num()
#FIXME: Finish compute_avg()
Avg: -1

''' Your solution goes here '''

user_num1 = 0
user_num2 = 0
avg_result = 0

user_num1 = get_user_num()
user_num2 = get_user_num()
avg_result = compute_avg(user_num1, user_num2)

print('Avg:', avg_result)


#Completed

def get_user_num():
    print('FIXME: Finish get_user_num()')
    return -1
def get_user_num():
    print('FIXME: Finish get_user_num()')
    return -1
def compute_avg(user_num1, user_num2):
    print('FIXME: Finish compute_avg()')
    return -1

user_num1 = 0
user_num2 = 0
avg_result = 0

user_num1 = get_user_num()
user_num2 = get_user_num()
avg_result = compute_avg(user_num1, user_num2)

print('Avg:', avg_result)
