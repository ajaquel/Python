user_age_years = int(input('enter your age in years:\n'))

user_age_days = user_age_years  * 365
user_age_minutes = user_age_days * 24 * 60
user_age_seconds = user_age_minutes * 60

user_heart_beats = user_age_minutes * 72

print('You are at least %d days old.' % user_age_days)
print('You are at least %d minutes old.' % user_age_minutes)
print('You are at least %d seconds old.' % user_age_seconds)
print('Your heart have beaten %d times.' % user_heart_beats)


