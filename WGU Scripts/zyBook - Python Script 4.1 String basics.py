#A 'Mad Libs' style game where user enters nouns,
#verbs, etc., and then a story using those words is ouput.

#Get user's words
relative = input('Enter a type of relative: ')
print()

food = input('Enter a type of food: ')
print()

adjective = input('Enter an adjective: ')
print()

period = input('Enter a time period: ')
print()

# Tell the story
print('My', relative, 'says eating', food)
print('will make me more', adjective)
print('so now I eat it every', period)



empty_string = ''
print("Empty String Value is =>", empty_string, "<= so?")




george_v = "His Majesty George V, by the Grace of God, " \
           "of the United Kingdom of Great Britain and " \
           "Ireland and of the British Dominions beyond " \
           "the Seas, King, Defender of the Faith, Emperor of India"
gandhi = 'Mohandas Karamchand Gandhi'
john_f_kennedy = 'JFK'

print(len(george_v), 'characters is much too long of a name!')
print(len(gandhi), 'characters is better...')
print(len(john_f_kennedy), 'characters is short enough.')



#Accessing positions
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(alphabet[0], alphabet[1], alphabet[25])


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
user_number = int(input('Enter number to use as index: '))
print()
print('\nLetter', user_number, 'of the alphabet is', alphabet[user_number])



#Strings are immutable and cannot be changed.


#Individual characters of a string cannot be directly changed.

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Change to upper case

alphabet[0] = 'A'  # Invalid: Cannot change character
alphabet[1] = 'B'  # Invalid: Cannot change character

print('Alphabet:', alphabet)


#Instead, update the variable by assigning an entirely new string.

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# Change to upper case
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('Alphabet:', alphabet)


#String concatenating
string_1 = 'abc'
string_2 = '123'
concatenated_string = string_1 + string_2
print('Easy as ' + concatenated_string)



#Type two statements. The first reads user input into person_name.
# The second reads user input into person_age. Use the int() function to
# convert person_age into an integer. Note: Do not write a prompt for the
# input values. Below is a sample output for the given program if the user's input is: Amy 4
#In 5 years Amy will be 9

person_name = ''
person_age = 0

person_name = input()
person_age = int(input())

print('In 5 years', person_name, 'will be', person_age + 5)


#Write two statements to read in values for my_city followed by my_state.
# Do not provide a prompt. Assign log_entry with current_time, my_city,
# and my_state. Values should be separated by a space. Sample output for
# given program if my_city is Houston and my_state is Texas:
#2014-07-26 02:12:18: Houston Texas

#Note: Do not write a prompt for the input values.
current_time = '2014-07-26 02:12:18:'
my_city = ''
my_state = ''
log_entry = ''

my_city = input()
my_state = input()
log_entry = current_time + ' ' + my_city + ' ' + my_state

print(log_entry)



