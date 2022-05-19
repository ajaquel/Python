
""" Computes the total cost of leasing a car given the down payment,
    monthly rate, and number of months """

down_payment = int(input('Enter down payment: '))
payment_per_month = int(input('Enter monthly payment: '))
num_months = int(input('Enter number of months: '))

total_cost = down_payment + (payment_per_month * num_months)

print ('Total cost:', total_cost)



#calculates average
num_sales1 = 3
num_sales2 = 4
num_sales3 = 8
avg_sales = 0

avg_sales = (num_sales1 + num_sales2 + num_sales3) / 3

print(avg_sales)


#Calculates sphere volume
pi = 3.14159
sphere_radius = 1.0
sphere_volume = 0.0

sphere_volume = (4.0 / 3.0) * (pi * (sphere_radius ** 3))

print(sphere_volume)




#Calculates gravity acceleration
G = 6.673e-11
M = 5.98e24
dist_center = 6.3782e6

accel_gravity = (G * M) / (dist_center ** 2)

print(accel_gravity)

