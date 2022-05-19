# A for loop over a dictionary retrieves each key in the dictionary.
for key in dictionary:  # Loop expression
    # Statements to execute in the loop

#Statements to execute after the loop




#dict.items()
num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda, calories in num_calories.items():
    print('%s: %d' % (soda, calories))


#dict.keys()
num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda in num_calories.keys():
    print(soda)


#dict.values()
num_calories = dict(Coke=90, Coke_zero=0, Pepsi=94)
for soda in num_calories.values():
    print(soda)




# Use list() to convert view objects into lists.
solar_distances = dict(mars=219.7e6, venus=116.4e6, jupiter=546e6, pluto=2.95e9)
list_of_distances = list(solar_distances.values())  # Convert view to list

sorted_distance_list = sorted(list_of_distances)
closest = sorted_distance_list[0]
next_closest = sorted_distance_list[1]

print('Closest planet is %.4e' % closest)
print('Second closest planet is %.4e' % next_closest)





# Write a program that uses the keys(), values(), and/or items() dict methods to find statistics about the student_grades dictionary. Find the following:
#
# Print the name and grade percentage of the student with the highest total of points.
# Find the average score of each assignment.
# Find and apply a curve to each student's total score, such that the best student has 100% of the total points.

# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}




# NOT TOO BAD BUT INCOMPLETE ANSWER
# student_grades contains scores (out of 100) for 5 assignments
student_grades = {
    'Andrew': [56, 79, 90, 22, 50],
    'Nisreen': [88, 62, 68, 75, 78],
    'Alan': [95, 88, 92, 85, 85],
    'Chang': [76, 88, 85, 82, 90],
    'Tricia': [99, 92, 95, 89, 99]
}

#Task 1
grades_comp = {}
for name, grades in student_grades.items():
    grades_sum = sum(grades)
    print('grades_sum:', name, grades_sum)
    grades_per = ((grades_sum * 100) / 500)
    grades_comp[name] = grades_per
print('grades_comp:', grades_comp)

sorted_grades_final_2 = sorted((grades,name) for (name,grades) in grades_comp.items())
print('sorted_grades_final_2:', sorted_grades_final_2)
highest = sorted_grades_final_2[-1]
print('highest:', highest)
print()

#grades_final = list(grades_comp.values())
#sorted_grades_final = sorted(grades_final)
#print('only grades_final:', sorted_grades_final)
#print('only highest grade:', sorted_grades_final[-1])
print()

print(student_grades.keys())
print(student_grades.values())
print(student_grades.items())





#Write a loop that prints each country's population in country_pop. Sample output for the given program:
# United States has 318463000 people.
# India has 1247220000 people.
# Indonesia has 252164800 people.
# China has 1365830000 people.

country_pop = {
    'China':         1365830000,
    'India':         1247220000,
    'United States': 318463000,
    'Indonesia':     252164800
} # country populations as of 2014

''' Your solution goes here '''

    print(country, 'has', pop, 'people.')



# Completed
country_pop = {
    'China':         1365830000,
    'India':         1247220000,
    'United States': 318463000,
    'Indonesia':     252164800
} # country populations as of 2014

for country, pop in country_pop.items(): # <- MY SOLUTION

    print(country, 'has', pop, 'people.')

