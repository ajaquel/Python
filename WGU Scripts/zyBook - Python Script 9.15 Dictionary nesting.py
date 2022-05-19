# Nested dictionaries.
students = {}
students ['Jose'] = {'Grade': 'A+', 'StudentID': 22321}

print('Jose:')
print(' Grade: %s' % students ['Jose']['Grade'])
print(' ID: %d' % students['Jose']['StudentID'])




# Nested dictionaries example: Storing grades.
grades = {
    'John Ponting': {
        'Homeworks': [79, 80, 74],
        'Midterm': 85,
        'Final': 92
    },
    'Jacques Kallis': {
        'Homeworks': [90, 92, 65],
        'Midterm': 87,
        'Final': 75
    },
    'Ricky Bobby': {
        'Homeworks': [50, 52, 78],
        'Midterm': 40,
        'Final': 65
    },
}

user_input = input('Enter student name: ')

while user_input != 'exit':
    if user_input in grades:
        # Get values from nested dict
        homeworks = grades[user_input]['Homeworks']
        midterm = grades[user_input]['Midterm']
        final = grades[user_input]['Final']

        # print info
        for hw, score in enumerate(homeworks):
            print('Homework %d: %d' % (hw, score))

        print('Midterm: %s' % midterm)
        print('Final: %s' % final)

        # Compute student total score
        total_points = sum([i for i in homeworks]) + midterm + final
        print('Final percentage: %f%%' % (100*(total_points / 500.0)))

    user_input = input('Enter student name: ')






# Nested dictionaries example: Music library.
# The following example demonstrates a program that uses 3
# levels of nested dictionaries to create a simple music library.
#
# The following program uses nested dictionaries to store a small
# music library. Extend the program such that a user can add artists,
# albums, and songs to the library. First, add a command that adds an
# artist name to the music dictionary. Then add commands for adding
# albums and songs. Take care to check that an artist exists in the
# dictionary before adding an album, and that an album exists before adding a song.

music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': [ 'Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973,
            'platinum': True
        },
        'The Wall': {
            'songs': [ 'Another Brick in the Wall', 'Mother', 'Hey you'],
            'year': 1979,
            'platinum': True
        }
    },
    'Justin Bieber': {
        'My World':{
            'songs': ['One Time', 'Bigger', 'Love Me'],
            'year': 2010,
            'platinum': True
        }
    }
}

# Get user input

# While user input != 'exit'
    # ...


