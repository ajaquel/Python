# Multiple except blocks.
try:
    # ... Normal code
except exceptiontype1:
    # ... Code to handle exceptiontype1
except exceptiontype2:
    # ... Code to handle exceptiontype2
...
except:
    # ... Code to handle other exception types






# BMI example with multiple exception types.
user_input = ''
while user_input != 'q':
    try:
        weight = int(input("Enter weight (in pounds): "))
        height = int(input("Enter height (in inches): "))

        bmi = (float(weight) / float(height * height)) * 703
        print('BMI:', bmi)
        print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov
    except ValueError:
        print('Could not calculate health info.\n')
    except ZeroDivisionError:
        print('Invalid height entered. Must be > 0.')

    user_input = input("Enter any key ('q' to quit): ")




# Multiple exception types in a single exception handler.
try:
    # ...
except (ValueError, TypeError):
    # Exception handler for any ValueError or TypeError that occurs.
except (NameError, AttributeError):
    # A different handler for NameError and AttributeError exceptions.
except:
    # A different handler for any other exception type.


