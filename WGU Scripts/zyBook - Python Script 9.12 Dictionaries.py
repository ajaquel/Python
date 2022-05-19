
student_grades = {}  # Create an empty dict
grade_prompt = "Enter name and grade (Ex. 'Bob A+'):"
menu_prompt = ("1. Add/modify student grade\n"
                "2. Delete student grade\n"
                "3. Print student grades\n"
                "4. Quit\n")

while True:  # Exit when user enters no input
    command = input(menu_prompt).lower().strip()
    if command == '1':
        name, grade = input(grade_prompt).split()
        student_grades[name] = grade
    elif command == '2':
        name, grade = input(grade_prompt).split()
        del student_grades[name]
    elif command == '3':
        print(student_grades)
        for i in student_grades:
            print((student_grades[i]))
    elif command == '4':
        break
    else:
        print('Unrecognized command.')






# Delete Prussia from country_capital. Sample output for the given program:
# Prussia deleted? Yes.

country_capital = {'Spain': 'Madrid', 'Togo': 'Lome', 'Prussia': 'Konigsberg'}
del country_capital['Prussia']
print('Prussia deleted?', end=' ')
if 'Prussia' in country_capital:
    print('No.')
else:
    print('Yes.')
