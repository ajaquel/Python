names = ['Daniel', 'Roxanna', 'Jean', 'Alejandro']
print(names)



# Some of the most expensive cars in the world
lamborghini_veneno = 3900000  # $3.9 million!
bugatti_veyron = 2400000      # $2.4 million!
aston_martin_one77 = 1850000  # $1.85 million!

prices = [lamborghini_veneno, bugatti_veyron, aston_martin_one77]

print('Lamborghini Veneno:', prices[0], 'dollars')
print('Bugatti Veyron Super Sport:', prices[1], 'dollars')
print('Aston Martin One-77:', prices[2], 'dollars')


#Modifying list
my_nums = [5, 12, 20]
print(my_nums)

# Modify a list element
my_nums[1] = -28
print (my_nums)




short_names = ['Gus', 'Bob', 'Zoe']

print(short_names[0])
print(short_names[1])
print(short_names[2])



# Concatenating lists
house_prices = [380000, 900000, 875000] + [225000]
print('There are', len(house_prices), 'prices in the list.')

# Finding min, max
print('Cheapest house:', min(house_prices))
print('Most expensive house:', max(house_prices))





#The following program calculates some information regarding final and midterm scores.
#Try enhancing the program by calculating the average midterm and final scores.

#Program to calculate statistics from student test scores.
midterm_scores = [99.5, 78.25, 76, 58.5, 100, 87.5, 91, 68, 100]
final_scores = [55, 62, 100, 98.75, 80, 76.5, 85.25]

#Combine the scores into a single list
all_scores = midterm_scores + final_scores

num_midterm_scores = len(midterm_scores)
num_final_scores = len(final_scores)

print(num_midterm_scores, 'students took the midterm.')
print(num_final_scores, 'students took the final.')

#Calculate the number of students that took the midterm but not the final
dropped_students = num_midterm_scores - num_final_scores
print(dropped_students, 'students must have dropped the class.')

lowest_final = min(final_scores)
highest_final = max(final_scores)

print('\nFinal scores ranged from', lowest_final, 'to', highest_final)

# Calculate the average midterm and final scores
# Hint: Sum the midterm scores and divide by number of midterm takers
#       Repeat for the final

sum_midterm = sum(midterm_scores)
print('The Average of Midterm Scores is:', sum_midterm / len(midterm_scores))

sum_final = sum(final_scores)
print('The Average of Final Scores is:', sum_final / len(final_scores))


#Using tuples
white_house_coordinates = (38.8977, 77.0366)
print('Coordinates:', white_house_coordinates)
print('Tuple length:', len(white_house_coordinates))

# Access tuples via index
print('\nLatitude:', white_house_coordinates[0], 'north')
print('Longitude:', white_house_coordinates[1], 'west\n')

# Error. Tuples are immutable
white_house_coordinates[1] = 50




team_names = ('Rockets', 'Raptors', 'Warriors', 'Celtics')

print(team_names[0])
print(team_names[1])
print(team_names[2])
print(team_names[3])


