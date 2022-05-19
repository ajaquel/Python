'''
A list can be useful in solving various engineering problems.
One problem is computing the voltage drop across a series of
resistors. If the total voltage across the resistors is V,
then the current through the resistors will be I = V/R, where R
is the sum of the resistances. The voltage drop Vx across resistor
x is then Vx = I · Rx.

zyDE 9.11.1: Calculate voltage drops across series of resistors.
The following program uses a list to store a user-entered set of
resistance values and computes I.

Modify the program to compute the voltage drop across each resistor,
store each in another list voltage_drop, and finally print the results
in the following format:

5 resistors are in series.
This program calculates the voltage drop across each resistor.
Input voltage applied to circuit: 12.0
Input ohms of 5 resistors
1) 3.3
2) 1.5
3) 2.0
4) 4.0
5) 2.2
Voltage drop per resistor is
1) 3.0 V
2) 1.4 V
3) 1.8 V
4) 3.7 V
5) 2.0 V

'''
num_resistors = 5
resistors = []
voltage_drop = []

print( '%d resistors are in series.' % num_resistors)
print('This program calculates the'),
print('voltage drop across each resistor.')

input_voltage = float(input('Input voltage applied to circuit: '))
print (input_voltage)

print('Input ohms of %d resistors' % num_resistors)
for i in range(num_resistors):
    res = float(input('%d)' % (i + 1)))
    print(res)
    resistors.append(res)

#  Calculate current
current = input_voltage / sum(resistors)
# Calculate voltage drop over each resistor
for i in range(num_resistors):
    vdrop = current * resistors[i]
    voltage_drop.append(int(vdrop))

# Print the voltage drop per resistor
for index, i in enumerate(voltage_drop):
    print('%d Resistor Voltage Drop is %f' % ((index + 1), i))







'''
Matrix multiplication of 4x2 and 2x3 matrices.
The following illustrates matrix multiplication for 4x2 and 2x3 matrices captured as two-dimensional lists.

Run the program below. Try changing the size and value of the matrices and computing new values.
'''


m1_rows = 4
m1_cols = 2
m2_rows = m1_cols  # Must have same value
m2_cols = 3

m1 = [
    [3, 4],
    [2, 3],
    [1, 2],
    [0, 2]
]

m2 = [
    [5, 4, 4],
    [0, 2, 3]
]

m3 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# m1 * m2 = m3
for i in range(m1_rows):  # for each row of m1
    for j in range(m2_cols):  # for each column of m2
        # Compute dot product
        dot_product = 0
        for k in range(m2_rows): #  for each row of m2
            dot_product += m1[i][k] * m2[k][j]

        m3[i][j] = dot_product

for i in range(m1_rows):
    for j in range(m2_cols):
        print('%2d' % m3[i][j], end=' ')
    print()  # Print single newline



