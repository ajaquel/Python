# String.format() example.
print('{0} is {1} years old'.format('Johnny', 18))



#Positional: An integer that describes the position of the value.
'The {1} in the {0}'.format('hat','cat')

#Inferred positional: Empty {} assumes ordering of replacement fields is {0}, {1}, {2}, etc.
'The {} in the {}'.format('cat', 'hat')

#Named: A name matching a keyword argument.
'The {animal} in the {headwear}'.format(animal='cat', headwear='hat')



# string.format() usage.

print('{hour}:{minute}'.format(hour=9, 43=minute))
#error


print('Hi {{{0}}}!'.format('Bilbo'))
Hi {Bilbo}!


month = 'April'
day = 22
print('Today is {month} {0}'.format(day, month=month))
Today is April 22
