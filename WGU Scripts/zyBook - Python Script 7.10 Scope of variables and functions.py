#The following program highlights the scope of variable total_inches.
cm_per_inch = 2.54
inches_per_foot = 12

def height_US_to_cm(feet, inches):
    """ Converts a height in feet/inches to centimeters."""
    total_inches = (feet * inches_per_foot) + inches  # Total inches
    cm = total_inches * cm_per_inch
    return cm

feet = int(input('Enter feet: '))
inches = int(input('Enter inches: '))

print('Centimeters:', height_US_to_cm(feet, inches))




#A global statement must be used to change the value of a global variable
# inside of a function. The following shows two programs: the right uses
# a global statement to allow the modification of global variable employee_name
# inside of the get_name function.
employee_name = 'N/A'

def get_name():
    name = input('Enter employee name:')
    employee_name = name

get_name()
print('Employee name:', employee_name)



employee_name = 'N/A'

def get_name():
    global employee_name
    name = input('Enter employee name:')
    employee_name = name

get_name()
print('Employee name:', employee_name)




#Error: Function definitions must be evaluated before that function is called.
employee_name = 'N/A'

get_name()
print('Employee name:', employee_name)

def get_name():
    global employee_name
    name = input('Enter employee name:')
    employee_name = name



