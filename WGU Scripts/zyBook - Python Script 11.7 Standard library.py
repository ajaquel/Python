#Using the datetime module.
#The datetime module prints the day, month, and year of a date that is a user-entered number of days in the future.

import datetime

# Create a new date object representing the current date (May 30, 2016)
today  = datetime.date.today()

days_from_now = int(input('Enter number of days from now: '))

# Create a new timedelta object that represents a difference in the
# number of days between dates.
day_difference = datetime.timedelta(days = days_from_now)

# Calculate new date
future_date = today + day_difference

print(days_from_now, 'days from now is', future_date.strftime('%B %d, %Y'))






#Using the random module.
#The random module is used to implement a simple game where a user continues
# to draw from a deck of cards until an ace card is found.
import random

# Create a shuffled card deck with 4 suites of cards 2-10, and face cards
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4
random.shuffle(deck)

num_drawn = 0
game_over = False
user_input = input("Press any key to draw a card ('q' to quit): ")
while user_input != 'q' and not game_over:

    # Draw a random card, and remove card from the deck
    card = random.choice(deck)
    deck.remove(card)
    num_drawn += 1

    print('\nCard drawn:', card)

    # Game is over if an ace was drawn
    if card == 'A':
        game_over = True
    else:
        user_input = input("Press any key to draw a card ('q' to quit): ")

if user_input == 'q':
    print("\nGame was quit")
else:
    print(num_drawn, 'card(s) drawn to find an ace.')





