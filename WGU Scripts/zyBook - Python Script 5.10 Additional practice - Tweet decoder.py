tweet = input('Enter abbreviation from tweet:\n')

if tweet == 'LOL':
    print('LOL = laughing out loud')
elif tweet == 'BFN':
    print('BFN = bye for now')
elif tweet == 'FTW':
    print('FTW = for the win')
elif tweet == 'IRL':
    print('IRL = in real life')
else:
    print("Sorry, don't know that one")



# Part 1: Expand the number of abbreviations that can be decoded.
# Part 2: Allow the user to enter a complete tweet (160 characters or less)
# as a single line of text. Search the resulting string for abbreviations and
# print a list of each abbreviation along with its decoded meaning.
# Part 3: Convert the user's tweet to a decoded tweet, replacing the abbreviations
# directly within the tweet.

#print('\nConverted tweet to lowercase is', tweet)

user_val = '-'

while user_val != 'q':
  tweet = input('User enter 160 characters or less tweet:\n').lower()
  if 'lol' in tweet:
    print('\nLOL = laughing out loud')
    decoded_tweet = tweet.replace('LOL', 'Laughing out loud')
    print(decoded_tweet)
  if 'bfn' in tweet:
    print('\nBFN = bye for now')
  if 'ftw' in tweet:
    print('\nFTW = for the win')
  if 'irl' in tweet:
    print('\nIRL = in real life')
  if 'ttyl' in tweet:
    print('\nTTYL = talk to you')
#else:
#    print("Sorry, don't know that one")
  user_input = input("\nEnter a character ('q' for quit or 'c' for continue): ")
  user_value = user_input[0]

