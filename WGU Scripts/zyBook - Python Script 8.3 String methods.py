#The following example uses the above function, asking the user to spell out
# numbers, and translating those numbers to another language.

user_input = input("Enter sentence:\n")

translation = user_input[:]  # Make a copy of the string

# Replace English with Spanish.
translation = translation.replace('one', 'uno')
translation  = translation.replace('two', 'dos')
translation = translation.replace('three', 'tres')
translation = translation.replace('four', 'quatro')
translation = translation.replace('five', 'cinco')
translation = translation.replace('six', 'seis')
translation  = translation.replace('seven', 'siete')
translation  = translation.replace('eight', 'ocho')
translation = translation.replace('nine', 'nueve')

print('Translation:', translation)



if 'b' in my_str:
    # Statements to execute if my_str contains a 'b' character.



# The following example carries out a simple guessing game, allowing a user
# a number of guesses to fill out the complete word.
word = 'onomatopoeia'
num_guesses = 10

hidden_word = '-' * len(word)

guess = 1

while guess <= num_guesses and '-' in hidden_word:
    print(hidden_word)
    user_input = input('Enter a character (guess #%d): ' % guess)

    if len(user_input) == 1:
        # Count the number of times the character occurs in the word
        num_occurrences = word.count(user_input)

        # Replace the appropriate position(s) in hidden_word with the actual character.
        position = -1
        for occurrence in range(num_occurrences):
            position = word.find(user_input, position+1)  # Find the position of the next occurrence
            hidden_word = hidden_word[:position] + user_input + hidden_word[position+1:]  # Rebuild the hidden word string

        guess += 1

if not '-' in hidden_word:
    print('Winner!', end=' ')
else:
    print('Loser!', end=' ')

print('The word was %s.' % word)



# Identity vs. equality operators.
student_name = input('Enter student name:\n')

if student_name is 'Kay, Jo':
    print('Identity operator: True')
else:
    print('Identity operator: False')

if student_name == 'Kay, Jo':
    print('Equality operator: True')
else:
    print('Equality operator: False')




# Run the program below and add some passengers into the database.
# Add a duplicate passenger name, using different capitalization,
# and print the list again.
menu_prompt = ('Available commands:\n'
               '  (add) Add passenger\n'
               '  (del) Delete passenger\n'
               '  (print) Print passenger list\n'
               '  (exit) Exit the program\n'
               'Enter command:\n')

destinations = ['PHX', 'AUS', 'LAS']

destination_prompt = ('Available destinations:\n'
                      '(PHX) Phoenix\n'
                      '(AUS) Austin\n'
                      '(LAS) Las Vegas\n'
                      'Enter destination:\n')

passengers = {}

print('Welcome to Mohawk Airlines!\n')
user_input = input(menu_prompt).strip().lower()

while user_input != 'exit':
    if user_input == 'add':
        name = input('Enter passenger name:\n').strip().upper()
        destination = input(destination_prompt).strip().upper()
        if destination not in destinations:
            print('Unknown destination.\n')
        else:
            passengers[name] = destination

    elif user_input == 'del':
        name = input('Enter passenger name:\n').strip().upper()
        if name in passengers:
            del passengers[name]

    elif user_input == 'print':
        for passenger in passengers:
            print('%s --> %s' % (passenger.title(), passengers[passenger]))
    else:
        print('Unrecognized command.')

    user_input = input('Enter command:\n').strip().lower()




#Complete the if-else statement to print 'LOL means laughing out loud'
# if user_tweet contains 'LOL'. Sample output from given program:

# LOL means laughing out loud.

user_tweet = 'I was LOL during the whole movie!'

''' Your solution goes here '''

    print('LOL means laughing out loud.')
else:
    print('No abbreviation.')



#Completed
user_tweet = 'I was LOL during the whole movie!'

if 'LOL' in user_tweet:

    print('LOL means laughing out loud.')
else:
    print('No abbreviation.')






# Assign decoded_tweet with user_tweet, replacing any occurrence of 'TTYL'
# with 'talk to you later'. Sample output from given program:
# Gotta go. I will talk to you later.

user_tweet = 'Gotta go. I will TTYL.'

decoded_tweet = """ Insert here you solution """
print(decoded_tweet)





# Completed
user_tweet = 'Gotta go. I will TTYL.'

decoded_tweet = user_tweet.replace('TTYL', 'talk to you later')
print(decoded_tweet)


