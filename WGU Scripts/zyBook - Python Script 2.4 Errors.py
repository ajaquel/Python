#2.4.1: A program with a syntax error.
print('Current salary is', end=' ')
print(45000)

print('Enter new salary:', end=' ')
new_sal = int(input())

print(new_sal) print(user_num)

#2.4.2: Runtime errors can crash the program.
print('Salary is', end=' ')
print(20 * 40 * 50)

print('Enter integer: ', end=' ')
user_num = int(input())
print(user_num)

#2.4.3: The programmer made a mistake that happens to be correct syntax, but has a different meaning.
current_salary = int(input('Enter current salary:'))

raise_percentage = 5  # Logic error gives a 500% raise instead of 5%.
new_salary = current_salary + (current_salary * raise_percentage)
print('New salary:', new_salary)


#2.4.1: Fix the bug.
num_beans = 500
num_jars = 3
total_beans = 0

print(num_beans, 'beans in', end=' ')
print(num_jars, 'jars yields', end=' ')
total_beans = num_beans * num_jars
print('total_beans', 'total')    #solution: remove single quotes from variable

#2.4.1: Basic syntax errors.
print('Predictions are hard.")
print(Especially about the future.)
user_num = 5
print('user_num is:' user_num)

#2.4.1: Basic syntax errors. FIXED!
print('Predictions are hard.')
print('Especially about the future.')
user_num = 5
print('user_num is:', user_num)