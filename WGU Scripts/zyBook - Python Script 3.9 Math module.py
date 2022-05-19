import math

num = 49
num_sqrt = math.sqrt(num)
print(num_sqrt)


num_people = 5
ten_generation_ancestors1 = 1024 * num_people
print(ten_generation_ancestors1)

ten_generation_ancestors2 = math.pow(2, 10) * num_people
print(ten_generation_ancestors2)


#Example of using a math function: Savings interest program.
#Note: Blank print statements are used to go to the next line after reading pre-entered input.
import math
base = float(input('Enter initial savings: '))
print()
rate = float(input('Enter annual interest % rate: '))
print()
years = int(input('Enter years that pass: '))
print()
total = base * math.pow(1 + (rate / 100), years)
print ('Savings after', years, 'years is', total)


#Exercises: Determine the final value of z.
x = 2.3
z = math.ceil(x)

x = 2.3
z = math.floor(x)

z = 4.5
z = math.pow(math.floor(z), 2.0)

z = 15.75
z = math.sqrt(math.ceil(z))

z = 4
z = math.factorial(z)




#Assign point_dist with the distance between point (x1, y1) and point (x2, y2).
# The calculation is: Distance = SquareRootOf( (x2 - x1)2 + (y2 - y1)2 ).
# Sample output for the given program is:

import math

x1 = 1.0
y1 = 2.0
x2 = 1.0
y2 = 5.0
point_dist = 0.0

point_dist = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

print('Points distance:', point_dist)


#Simple geometry can compute the height of an object from the object's shadow length and shadow angle using the formula:
# tan(angleElevation) = treeHeight / shadowLength.
# Given the shadow length and angle of elevation, compute the tree height. Sample output for the given program is:
import math

angle_elev  = 3.8
shadow_len  = 17.5
tree_height = 0.0

tree_height = math.tan(angle_elev) * shadow_len

print('Tree height:', tree_height)


