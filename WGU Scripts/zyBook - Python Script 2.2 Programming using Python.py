#2.2.3: Executing a simple Python program.
wage = 20
hours = 40
weeks = 50
salary = wage * hours * weeks

print('Salary is:', salary)

hours = 35
salary = wage * hours * weeks
print('New salary is:', salary)

#2.2.1: A first program.
# Welcome to the Python 500 race! Click the run button to begin.

# Configurable values.
# Try changing car speeds, accelerations, and the simulation speed.
car1_top_speed = 60
car2_top_speed = 50

car1_acceleration = 11
car2_acceleration = 10

car1 = ['  ______\n',
        ' |__1_|_\\\n',
        '  O----O\n']

car2 = ['    ___\n',
        '   /__2_\\__\n',
        '    O----O\n']

# Begin program below.

# Track the location and speed of each car
car1_location = 0
car2_location = 0
car1_speed = 0
car2_speed = 0

track_length = 1000  # Length of the race
cols = 60  # Width of the output window


def print_car(car, distance):
    """Print a car at a scaled distance from the left side of the screen"""
    scale = float(distance) / float(track_length) * cols
    for line in car:
        print(' ' * int(scale), line, end=' ')


def print_cars():
    """Print each of the racing cars"""
    print_car(car1, car1_location)
    print_car(car2, car2_location)


def max_car_len():
    return max(max([len(i) for i in car1], [len(i) for i in car2]))


def print_finish():
    """Print the finish line"""
    ln = "||--FINISH LINE--||"
    print(' ' * (cols + max_car_len() - len(ln)), end=' ')
    print(ln)


def advance_cars():
    """Calculate new positions of the cars"""
    global car1_speed, car1_location
    global car2_speed, car2_location
    car1_speed += car1_acceleration
    car1_speed = car1_top_speed if car1_speed > car1_top_speed else car1_speed
    car1_location += car1_speed

    car2_speed += car2_acceleration
    car2_speed = car2_top_speed if car2_speed > car2_top_speed else car2_speed
    car2_location += car2_speed


def finished():
    """Check for a winner"""
    if car1_location > track_length or car2_location > track_length:
        if car1_location > car2_location:
            win_distance = car1_location - car2_location
            print('Car 1 wins by', win_distance, 'meters!')
        else:
            win_distance = car2_location - car1_location
            print('Car 2 wins by', win_distance, 'meters!')
        return True
    return False


while not finished():
    """Main loop"""
    advance_cars()

print_cars()
print_finish()


