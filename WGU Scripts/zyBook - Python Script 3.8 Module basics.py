# The baby_names.py module

print ('Initializing baby variables...')
baby_name1 = 'Ryder'
baby_name2 = 'Jess'
baby_weight1 = 5.1
baby_weight2 = 8.5

# Executes only if file run as a script (e.g., python baby_names.py)
if __name__ == '__main__':
    print('Baby 1:', baby_name1, 'was born', baby_weight1, 'lbs')
    print('Baby 2:', baby_name2, 'was born', baby_weight2, 'lbs')
 # A script favorite_child.py that imports and uses the baby_names module.

import baby_names  # Importing the module executes the module contents

print('My favorite child is', baby_names.baby_name1, '-')
print('I remember when he weighed only', baby_names.baby_weight1, 'pounds.')
print('I love', baby_names.baby_name2, 'too, of course.')



# Gravitational constants for various planets

earth_g = 9.81  # m/s^2
mars_g = 3.71

if __name__ == '__main__':
    print('Earth constant:', earth_g)
    print('Mars constant:', mars_g)


# Find seconds to drop from a height on some planets.
import constants
import math

height = int(input('Height in meters: '))  # Meters from planet

if __name__ == '__main__':
    print('Earth:', math.sqrt(2 * height / constants.earth_g), 'seconds')
    print('Mars:', math.sqrt(2 * height / constants.mars_g), 'seconds')
