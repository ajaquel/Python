#2.3.1: Printing text and new lines.
# Each print statement starts on a new line
print('Hello there.')
print('My name is...')
print('Carl?')

# Including end=' ' keeps output on same line
print('Hello there.', end=' ')
print('My name is...', end=' ')
print('Carl?')

#2.3.1: Output simple text.
print('3', '2', '1', 'Go!')

#2.3.2: Output an eight with asterisks.
print('*****')
print('*   *')
print('*****')
print('*   *')
print('*****')

#2.3.2: Printing the value of a variable.
wage = 20

print('Wage is', end=' ')
print(wage)  # print variable's value
print('Goodbye.')

#2.3.3: Printing multiple items using a single print statement.
wage = 20

print('Wage:', wage)  # Comma separates multiple items
print('Goodbye.')

#2.3.4: Printing using newline characters.
print('1\n2\n3')

#2.3.5: printing without text.
print('123')
print()
print('abc')


#2.3.3: Enter the output.
person_age = 23
print('Ann is', person_age, 'years.')


#2.3.7: A program can get an input value from the keyboard.
print('Enter name of best friend:', end=' ')
best_friend = input()
print('My best friend is', best_friend)

#2.3.6: Using int() to convert strings to integers.
my_string = '123'
my_int = int('123')

print(my_string)
print(my_int)

#2.3.7: Converting user input to integers.
print('Enter wage:', end=' ')
wage = int(input())

new_wage = wage + 10
print('New wage:', new_wage)

#2.3.8: Basic input example.
hours = 40
weeks = 50
hourly_wage = int(input('Enter hourly wage: '))

print('Salary is', hourly_wage * hours * weeks)

#2.3.1: Basic input.
dog_years = int(input('Enter age of dog (in years): '))
print()

human_years = 7 * dog_years

print(dog_years, 'dog years is about', end=' ')
print (human_years, 'human years.')

#2.3.4: Read user input and print to output.
num1 = int(input())
num2 = int(input())
num3 = int(input())
print(num1 * num2 * num3)

#2.3.5: Read user input numbers and perform a calculation.
num1 = int(input())
num2 = int(input())
print(num1 + num2)