
def compute_square(num_to_square):
    return num_to_square * num_to_square

num_squared = 0
num_squared = compute_square(7)

print('7 squared is', num_squared)



def square_root(x):
    return math.sqrt(x)

def print_val(x):
    print(x)
    return



#Program with a function to convert height in feet/inches to centimeters.
cm_per_inch = 2.54
inches_per_foot = 12

def height_US_to_cm(feet, inches):
    """Converts height in feet/inches to centimeters"""
    total_inches = feet * inches_per_foot + inches
    cm = total_inches * cm_per_inch
    return cm

feet = int(input('Enter feet: '))
inches = int(input('Enter inches: '))

print('Centimeters:', height_US_to_cm(feet, inches))




#Complete the program by writing and calling a function that converts a
# temperature from Celsius into Fahrenheit. Use the formula F = C x 9/5 + 32.
# Test your program knowing that 50 Celsius is 122 Fahrenheit.

def c_to_f():
    # FIXME
    return  # FIXME: Finish

temp_c = float(input('Enter temperature in Celsius: '))
temp_f = None

# FIXME: Call conversion function
# temp_f = ??

# FIXME: Print result
# print('Fahrenheit:' , temp_f)


#Completed
def c_to_f(temp_c):
    temp_f = (temp_c * 9/5) + 32
    return temp_f

temp_c = float(input('Enter temperature in Celsius: '))

print('\nFahrenheit:' , c_to_f(temp_c))




#Assign max_sum with the max of (num_a, num_b) PLUS the max of (num_y, num_z).
# Use just one statement. Hint: Call find_max() twice in an expression.
def find_max(num_1, num_2):
   max_val = 0.0

   if (num_1 > num_2):  # if num1 is greater than num2,
      max_val = num_1   # then num1 is the maxVal.
   else:                # Otherwise,
      max_val = num_2   # num2 is the maxVal
   return max_val

num_a = 5.0
num_b = 10.0
num_y = 3.0
num_z = 7.0
max_sum = 0.0

max_sum = find_max(num_a, num_b) + find_max(num_y, num_z)

print('max_sum is:', max_sum)




#Define a function pyramid_volume with parameters base_length,
# base_width, and pyramid_height, that returns the volume of a pyramid with a rectangular base.
# Relevant geometry equations:
# Volume = base area x height x 1/3
# Base area = base length x base width.

def pyramid_volume(base_length, base_width, pyramid_height):
    base_area = base_length * base_width
    pyramid_vol = base_area * pyramid_height * 1/3
    return pyramid_vol

print('Volume for 4.5, 2.1, 3.0 is:', pyramid_volume(4.5, 2.1, 3.0))




