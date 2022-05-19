#A programmer can examine the names in the current local and global namespace
# by using the  locals() and globals() built-in functions.
# Using the globals() to get namespace names.

print('Initial global namespace: ')
print(globals())

my_var = "This is a variable"
print('\nCreated new variable')
print(globals())

def my_func():
    pass

print('\nCreated new function')
print(globals())





daily_cals = 2300  # Daily calories
soda_cals = 200

def drink_soda(cals_left):
    return cals_left - soda_cals

daily_cals = drink_soda(daily_cals)




#Given the following program, select the namespace that each name would belong to.
import random

player_name = 'Gandalf'
player_type = 'Wizard'

def roll():
    """Returns a roll of a 20-sided die"""
    number = random.randint(1, 20)
    return number

print('A troll attacks!')
troll_roll = roll()
player_roll = roll()

print('Player: %s    Troll: %s' % (str(player_roll), str(troll_roll)))


