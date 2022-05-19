# First code block has no indentation

model = input('Enter car model: ')
year = int(input('Enter year of car manufacture: '))

antique = False
domestic = False

if year < 1970:
    # New code block has indentation of 4 columns
    antique = True

# Back to code block 0

if model in ['Ford', 'Chevrolet', 'Dodge']:
  # New code block has indentation of 2 columns
  # Any amount of indentation > 0 is OK.
  domestic = True

# Back to code block 0

if antique:
    # New code block has indentation of 4 columns
    if domestic:
        # New block has 4 additional columns (8 total)
        print('My own model-T still runs like a charm...')






# Calculate the velocity required to escape a circular orbit of Earth,
# depending on a user-entered orbital distance.

import math

escape_velocity_meters_per_sec = 0  # Required velocity to escape orbit
earth_grav_constant = 6.67384e-11   # Earth's gravitational constant
earth_mass_kilograms = 5.972e24      # Mass of the Earth

radius_meters = float(input('Enter distance from center of Earth: '))
print()

if radius_meters < 160000:  # 160 km is minimal low-earth orbit
    escape_velocity_meters_per_sec = 0  # No escape possible!
    print('Houston, we have a problem')


else:
    standard_grav_param = earth_grav_constant * earth_mass_kilograms
    escape_velocity_meters_per_sec = math.sqrt(2*standard_grav_param / radius_meters)
    print('Thrust to %d m/s to escape these Earthly shackles.' % escape_velocity_meters_per_sec)




declaration = ("When in the Course of human events, it becomes necessary for "
               "one people to dissolve the political bands which have connected "
               "them with another, and to assume among the powers of the earth...")
result_of_power = math.pow(long_variable_name_left_operand,
                           long_variable_name_right_operand)




my_list = [
    1, 2, 3,
    4, 5, 6
    ]


my_dict = {
    'entryA': 1,
    'entryB': 2
}



#Retype the below code. Fix the indentation as necessary to make the program work.
temperatures = {
    'Seattle': 56.5,
    'New York': 105,
    'Kansas City': 81.9,
    'Los Angeles': 76.5
}

    if 'New York' in temperatures:
        if temperatures['New York'] > 90:
        print('The city is melting!')
        else:
            print('The temperature in New York is', temperatures['New York'])
else:
        print('The temperature in New York is unknown.')



#Fixed Indentation
temperatures = {
    'Seattle': 56.5,
    'New York': 105,
    'Kansas City': 81.9,
    'Los Angeles': 76.5
}

if 'New York' in temperatures:
    if temperatures['New York'] > 90:
        print('The city is melting!')
    else:
        print('The temperature in New York is', temperatures['New York'])
else:
    print('The temperature in New York is unknown.')


