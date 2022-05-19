# Basic exception handling constructs.
try:
    # ... Normal code that might produce errors
except: # Go here if <i>any</i> error occurs in try block
    # ... Exception handling code





# BMI example without exception handling.
user_input = ''
while user_input != 'q':
    weight = int(input("Enter weight (in pounds): "))
    height = int(input("Enter height (in inches): "))

    bmi = (float(weight) / float(height * height)) * 703
    print('BMI:', bmi)
    print('(CDC: 18.6-24.9 normal)\n')
    # Source www.cdc.gov

    user_input = input("Enter any key ('q' to quit): ")




# BMI example with exception handling using try/except.
user_input = ''
while user_input != 'q':
    try:
        weight = int(input("Enter weight (in pounds): "))
        height = int(input("Enter height (in inches): "))

        bmi = (float(weight) / float(height * height)) * 703
        print('BMI:', bmi)
        print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov
    except:
        print('Could not calculate health info.\n')

    user_input = input("Enter any key ('q' to quit): ")




