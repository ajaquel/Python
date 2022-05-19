# Splitting a string into tokens.

string = "Music/artist/song.mp3"
my_tokens = string.split('/')


string = "I love python"
my_tokens = string.split()


url = input('Enter URL:\n')
tokens = url.split('/')  # Uses '/' separator
print(tokens)




file = 'C:/Users/Charles Xavier//Documents//report.doc'

separator = '/'
results = file.split(separator)
print('Separator (%s):' % separator, results)



# String join example: Comparing join vs. loops.
phrases = ['To be, ', 'or not to be.\n', 'That is the question.']

sentence = ''
for phrase in phrases:
    sentence += phrase
print(sentence)


phrases = ['To be, ', 'or not to be.\n', 'That is the question.']

sentence = ''.join(phrases)
print(sentence)



#Splitting and joining: Replacing separators.
path = input('Enter file name: ')

new_separator = input('Enter new separator: ')
tokens = path.split('/')
print(new_separator.join(tokens))




#Splitting and joining: Editing tokens.
url = input('Enter Wikipedia URL: ')

tokens = url.split('/')

if 'wiki' !=  tokens[3]:
    tokens.insert(3, 'wiki')
    new_url = '/'.join(tokens)

    print('%s not a valid address.' % url)
    print('Redirecting to %s' % new_url)
else:
    print('Loading %s' % url)




# Assign number_segments with phone_number split by the hyphens.
# Sample output from given program: Area code: 977

phone_number = '977-555-3221'
number_segments = phone_number.split('-')
area_code = number_segments[0]
print('Area code:', area_code)




