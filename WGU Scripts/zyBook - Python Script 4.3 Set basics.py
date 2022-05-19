# Create a set using the set() function.
nums1 = set([1, 2, 3])

# Create a set using a set literal.
nums2 = { 7, 8, 9 }

# Print the contents of the sets.
print(nums1)
print(nums2)




# Initial list contains some duplicate values
first_names = [ 'Harry', 'Hermione', 'Ron', 'Harry', 'Albus', 'Ron', 'Ron' ]

# Creating a set removes any duplicate values
names_set = set(first_names)

print(names_set)




# Remove 'Oliver' from the set, and add 'Atlas'.
male_names = { 'Oliver', 'Declan', 'Henry' }

male_names.remove('Oliver')
male_names.add('Atlas')



#The following program includes fictional sets of the top 10 male and female baby names
# for the current year. Write a program that creates:
# A set all_names that contains all of the top 10 male and all of the top 10 female names.
# A set neutral_names that contains only names found in both male_names and female_names.
# A set specific_names that contains only gender specific names.

male_names = { 'John', 'Bailey', 'Charlie', 'Chuck', 'Michael', 'Samuel', 'Jayden', 'Aiden', 'Henry', 'Lucas' }
female_names = { 'Elizabeth', 'Meghan', 'Kim', 'Khloe', 'Bailey', 'Jayden', 'Aiden', 'Britney', 'Veronica', 'Maria' }

# Use set methods to create sets all_names, neutral_names, and specific_names.

all_names = male_names.union(female_names)
neutral_names = male_names.intersection(female_names)
specific_names = male_names.symmetric_difference(female_names)

print(sorted(all_names))
print(sorted(neutral_names))
print(sorted(specific_names))
