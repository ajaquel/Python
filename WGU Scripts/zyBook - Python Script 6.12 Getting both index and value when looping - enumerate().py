origins = [4, 8, 10]

for index in range(len(origins)):
    value = origins[index]  # Retrieve value of element in list.
    print('Element %d: %s' % (index, value))



origins = [4, 8, 10]

for value in origins:
    index = origins.index(value)  # Retrieve index of value in list
    print('Element %d: %s' % (index, value))



origins = [4, 8, 10]

for (index, value) in enumerate(origins):
    print('Element %d: %s' % (index, value))

