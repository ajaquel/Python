# PV = nRT. Compute the temperature of a gas.
gas_constant = 8.3144621  # Joules / (mol*Kelvin)

def convert_to_temp(pressure, volume, mols):
    """Convert pressure, volume, and moles to a temperature"""
    return (pressure * volume) / (mols * gas_constant)

press = float(input('Enter pressure (in Pascals): '))
vol = float(input('Enter volume (in cubic meters): '))
mols = float(input('Enter number of moles: '))

print('Temperature = {:.2f} K'.format(convert_to_temp(press, vol, mols)))





# Trajectory of object on Earth.
import math

def trajectory(t, a, v, g, h):
    """Calculates new x,y position"""
    x = v * t * math.cos(a)
    y = h + v * t * math.sin(a) - 0.5 * g * t * t
    return (x,y)

def degree_to_radians(degrees):
    """Converts degrees to radians"""
    return ((degrees * math.pi) / 180.0)

gravity = 9.81 # Earth gravity (m/s^2)
time = 1.0 # time (s)
x_loc = 0
h = 0

angle = float(input('Launch angle (deg): '))
print(angle)
angle = degree_to_radians(angle)

velocity = float(input('Launch velocity (m/s): '))
print(velocity)

height = float(input('Initial height (m): '))
y_loc = height
print(y_loc)

while ( y_loc >= 0.0 ): # While above ground
    print('Time %3d x = %3d y = %3d' % (time, x_loc, y_loc))
    x_loc, y_loc = trajectory(time, angle, velocity, gravity, height)
    time += 1.0




#Define a function compute_gas_volume that returns the volume of a gas
# given parameters pressure, temperature, and moles. Use the gas equation
# PV = nRT, where P is pressure in Pascals, V is volume in cubic meters,
# n is number of moles, R is the gas constant 8.3144621 ( J / (mol*K)),
# and T is temperature in Kelvin.
gas_const = 8.3144621

''' Your solution goes here '''

gas_pressure = 100.0
gas_moles = 1.0
gas_temperature = 273.0
gas_volume = 0.0

gas_volume = compute_gas_volume(gas_pressure, gas_temperature, gas_moles)
print('Gas volume:', gas_volume, 'm^3')



#Completed
gas_const = 8.3144621

def compute_gas_volume(gas_pressure, gas_temperature, gas_moles):
    g_vol = gas_moles * gas_const * gas_temperature / gas_pressure
    return g_vol

gas_pressure = 100.0
gas_moles = 1.0
gas_temperature = 273.0
gas_volume = 0.0

gas_volume = compute_gas_volume(gas_pressure, gas_temperature, gas_moles)
print('Gas volume:', gas_volume, 'm^3')





