#----------------------------------------------------------
'''
def is_last_character_n(word):
    if (word[-1]) == 'n':
        r = True
    else:
        r = False
    print(r)
    return r
#    print(word[-1])
is_last_character_n("hello")
'''
#----------------------------------------------------------
'''
def num_to_dashes(num):
    r = '-' * num
    print(r)
    return('')

num_to_dashes(5)
'''
#----------------------------------------------------------
'''
def hello_name(name):
    print('"' + 'Hello ' + name + '!' + '"')
    return('')

hello_name('Bob')
'''
#----------------------------------------------------------
'''
def first_last(lst):
    r = (lst[0], lst[-1])
    print(r)
    return r

first_last([15, 10, 15, 20, 253])
'''
#----------------------------------------------------------
'''
t = (1,2,3,4,5)
l = [1,2,3,4,5]
s = {1,2,3,4,5}

print('t is: ', type(t))
print('l is: ', type(l))
print('s is: ', type(s))

if type(t) is tuple:
    t = list(t)
    if type(l) is list:
        l = set(l)
        if type(s) is set:
            s = tuple(s)

print('now t is: ', type(t))
print('now l is: ', type(l))
print('now s is: ', type(s))
'''
#----------------------------------------------------------
'''
def calculate_exponent(num, exp):
    for i in range(exp):
        print(range(exp))
        r = num * i
        print(r)
        return('')

calculate_exponent(5, 5)
'''
#----------------------------------------------------------

'''
def hello_world(num):
    if num % 3 == 0 and num % 5 == 0:
        print(num)
        return 'Hello'
    elif num % 5 == 0:
        print(num)
        return 'World'
    elif num % 3 == 0:
        print(num)
        return 'Hello'

hello_world(10)
'''
#----------------------------------------------------------
'''
def word_lengths(lst):
    print(lst)
    r = []
    for i in lst:
        print(len(i))
        r.append(len(i))
        print(r)
    return r

word_lengths(['hello', 'world'])
'''
#----------------------------------------------------------

'''
def add_up_to(n):
    print(n)
    l = []
    for i in range(n+1):
        l.append(i)
    print(l)
    print(sum(l))
add_up_to(3)
'''
#----------------------------------------------------------

'''
def is_truthy(val):
    if val == 'False' or val == False or val == 'none' or val == '0' or val == 0 or val == [] or val == {} or val == "":
        print('False')
        return False
    else:
        print('True')
        return True

is_truthy(1)
'''
#----------------------------------------------------------

'''
def get_triangle_type(lst):
	a = lst[0]
	b = lst[1]
	c = lst[2]
	print(lst)
	print(a,b,c)
	print(len(lst))
	if len(lst) > 3:
		print('not a triangle')
		return 'not a triangle'
	else:
		if a != b and a != c and b != c:
			print('scalene')
			return 'scalene'
		elif a == b and a != c and b != c:
			print('isosceles')
			return 'isosceles'
		elif  a != b and a == c and b != c:
			print('isosceles')
			return 'isosceles'
		elif a == b and a == c and b == c:
			print('equilateral')
			return 'equilateral'

get_triangle_type([2, 3, 4])
'''
#----------------------------------------------------------

username = "Connie"
code = "C859"
print('Welcome to {}, {}.'.format(code, username))
print('Welcome to %s, %s.' % (code, username) )

#----------------------------------------------------------



#----------------------------------------------------------



#----------------------------------------------------------



#----------------------------------------------------------



#----------------------------------------------------------



