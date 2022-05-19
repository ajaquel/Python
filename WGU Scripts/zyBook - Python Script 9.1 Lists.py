#Consider the following program that allows a user to print the age of the
# Nth oldest known person to have ever lived. Note: The ages are in a list
# sorted from oldest to youngest.

#1. Modify the program to print the correct ordinal number ("1st", "2nd",
# "3rd", "4th", "5th") instead of "1th", "2th", "3th", "4th", "5th".
#2. For the oldest person, remove the ordinal number (1st) from the
# print statement to say, "The oldest person lived 122 years".

#Reminder: List indices begin at 0, not 1, thus the print statement uses
# oldest_people[nth_person-1], to access the nth_person element (element
# 1 at index 0, element 2 at index 1, etc.).

oldest_people = [122, 119, 117, 117, 116]  # Source: Wikipedia.org

nth_person = int(input('Enter N (1-5): '))

if (nth_person >= 1) and (nth_person <= 5):
    print('The %dth oldest person lived %d years' % \
          (nth_person, oldest_people[nth_person-1]))



# In-place modification of a list.
my_teams = ['Raptors', 'Heat', 'Nets']
your_teams = my_teams  # Create a shared reference to same list

my_teams[1] = 'Lakers'  # Modify list element

print('My teams are:', my_teams)  # Both variables have changed
print('Your teams are:', your_teams)  # Both variables have changed



# In-place modification of a copy of a list.
my_teams = ['Raptors', 'Heat', 'Nets']
your_teams = my_teams[:]  # Assign your_teams to a COPY of my_teams

my_teams[1] = 'Lakers'  # Modify list element

print('My teams are:', my_teams)  # List element has changed
print('Your teams are:', your_teams)  # List element has not changed



# Modify short_names by deleting the first element and changing the last element to Joe.
short_names = ['Gertrude', 'Sam', 'Ann', 'Joseph']

short_names[3] = 'Joe'
del short_names[0]

print(short_names)

