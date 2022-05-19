# For example, a programmer might have developed and tested a function to
# convert a temperature value in Celsius to Fahrenheit, and then copied
# and modified the original function into a new function to convert Fahrenheit
# to Celsius as shown:
def cel_to_fah(celsius):
    tmp = (9.0/5.0) * celsius
    fah = tmp + 32

    return fah


def fah_to_cel(fah):
    tmp = fah - 32
    cel = tmp * (5.0/9.0)

    return fah



# Wrong Return variable specified.
def cel_to_fah(celsius):
    tmp = (9.0/5.0) * celsius
    fah = tmp + 32

    return tmp




# Missing return
def steps_to_feet(num_steps):
    feet_per_step = 3

    feet = num_steps * feet_per_step

feet_per_mile = 5280
steps = int(input('Enter number of steps walked: '))

feet = steps_to_feet(steps)
print("Distance walked in feet:", feet)





#Using the celsius_to_kelvin function as a guide, create a new function,
# changing the name to kelvin_to_celsius, and modifying the function accordingly.
def celsius_to_kelvin(value_celsius):
    value_kelvin = 0.0

    value_kelvin = value_celsius + 273.15
    return value_kelvin

def kelvin_to_celsius(value_kelvin):
    value_celsius = 0.0

    value_celsius = value_kelvin - 273.15
    return value_celsius

value_c = 0.0
value_k = 0.0

value_c = 10.0
print(value_c, 'C is', celsius_to_kelvin(value_c), 'K')

value_k = 283.15
print(value_k, 'is', kelvin_to_celsius(value_k), 'C')



