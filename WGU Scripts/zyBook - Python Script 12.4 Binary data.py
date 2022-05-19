# Creating a bytes object using a bytes literal.
my_bytes = b'This is a bytes literal'

print(my_bytes)
print(type(my_bytes))



# Byte string literals.
print(b'123456789 is the same as \x31\x32\x33\x34\x35\x36\x37\x38\x39')



# Inspecting the binary contents of an image file.
f = open('ball.bmp', 'rb')  # Open in binary mode using 'b'

# Read image binary data
contents = f.read()

print('Contents of ball.bmp\n')
print(contents)

f.close()



# Altering a BMP image file.
# The following program reads in ball.bmp, overwrites a portion of the
# image with new pixel colors, and creates a new image file. Download the
# above image (right click the image --> save), and then run the program
# on your own computer, creating a new, altered version of ball.bmp. Try
# changing the alterations made by the program to get different colors.

import struct

ball_file = open('ball.bmp', 'rb')
ball_data = ball_file.read()
ball_file.close()

# BMP image file format stores location
# of pixel RGB values in bytes 10-14
pixel_data_loc = ball_data[10:14]

# Converts byte sequence into integer object
pixel_data_loc = struct.unpack('<L', pixel_data_loc)[0]

# Create sequence of 3000 red, green, and yellow pixels each
new_pixels = b'\x01'*3000 + b'\x02'*3000 + b'\x03'*3000

# Overwrite pixels in image with new pixels
new_ball_data = ball_data[:pixel_data_loc] + \
              new_pixels + \
              ball_data[pixel_data_loc + len(new_pixels):]

# Write new image
new_ball_file = open('new_ball.bmp', 'wb')
new_ball_file.write(new_ball_data)
new_ball_file.close()





# Packing values into byte sequences.
import struct

print('Result of packing 5:', end=' ')
print(struct.pack('>h', 5))

print('Result of packing 256:', end=' ')
print(struct.pack('>h', 256))

print('Result of packing 5 and 256:', end=' ')
print(struct.pack('>hh', 5, 256))




# Unpacking values from byte sequences.
import struct

print('Result of unpacking %s:' % repr('\x00\x05'), end=' ')
print(struct.unpack('>h', b'\x00\x05'))


print('Result of unpacking %s:' % repr('\x01\x00'), end=' ')
print(struct.unpack('>h', b'\x01\x00'))

print('Result of unpacking %s:' % repr('\x00\x05\x01\x00'), end=' ')
print(struct.unpack('>hh', b'\x00\x05\x01\x00'))




