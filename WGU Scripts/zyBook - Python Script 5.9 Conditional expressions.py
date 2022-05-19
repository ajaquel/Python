# Create a conditional expression that evaluates to string "negative" if user_val
# is less than 0, and "non-negative" otherwise. Example output when user_val is -9
# for the below sample program:
user_val = -9

cond_str = 'negative' 
if user_val < 0:
    cond_str = 'negative'
else:
    cond_str = 'non-negative'

print(user_val, 'is', cond_str)



# Using a conditional expression, write a statement that increments num_users if
# update_direction is 3, otherwise decrements num_users. Ex: if num_users is 8
# and update_direction is 3, then num_users becomes 9; if update_direction is 0,
# then num_users becomes 7.
num_users = 8
update_direction = 3

num_users = num_users
if update_direction == 3:
    num_users = num_users + 1
else:
    num_users = num_users - 1

print('New value is:', num_users)



