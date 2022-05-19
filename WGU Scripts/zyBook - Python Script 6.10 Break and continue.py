#In the example below, the nested for loops generate all possible meal options for the
# number of empanadas and tacos that can be purchased. The inner loop body calculates
# the cost of the current meal option. If the meal cost is equal to the user's amount
# of money, the search is over, so the break statement immediately exits the inner loop.
# The outer loop body also checks if the meal cost and the user's amount of money are
# equal, and if so, that break statement exits the outer loop. The program could be
# written without break statements, but the loops' condition expressions would be more
# complex and the program would require additional code, perhaps being harder to understand.

empanada_cost = 3
taco_cost = 4

user_money = int(input('Enter money for meal: '))

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost
print('max_empanadas:', max_empanadas)
print('max_tacos:', max_tacos)
meal_cost = 0
for num_tacos in range(max_tacos + 1):
    print('num_tacos:', num_tacos)
    for num_empanadas in range(max_empanadas + 1):
        print('num_empanadas:', num_empanadas)
        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)
        print('meal_cost:', meal_cost)

        # Find first meal option that exactly matches user money
        if meal_cost == user_money:
            break

    # Find first meal option that exactly matches user money
    if meal_cost == user_money:
        break

if meal_cost == user_money:
    print('$%d buys %d empanadas and %d tacos without change.' %
        (meal_cost, num_empanadas, num_tacos))
else:
    print('You cannot buy a meal without having change left over.')






#The program uses two nested for loops to try all possible combinations of tacos
# and empanadas. If the total number of tacos and empanadas is not exactly divisible
# by the number of diners (e.g., num_tacos + num_empanadas) % num_diners != 0,
# the continue statement will immediately proceed to the next iteration of the for
# loop. Break and continue statements can be helpful to avoid excessive indenting/nesting
# within a loop. However, because someone reading a program could easily overlook a break
# or continue statement, such statements should be used only when their use is clear to the reader.

empanada_cost = 3
taco_cost = 4

user_money = int(input('Enter money for meal: '))

num_diners = int(input('How many people are eating: '))

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

meal_cost = 0
num_options = 0
for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):

        # Total items purchased must be equally divisible by number of diners
        if (num_tacos + num_empanadas) % num_diners != 0:
            continue

        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

        if meal_cost == user_money:
            print('$%d buys %d empanadas and %d tacos without change.' %
                  (meal_cost, num_empanadas, num_tacos))
            num_options += 1

if num_options == 0:
    print('You cannot buy a meal without having change left over.')





#Simon Says" is a memory game where "Simon" outputs a sequence of 10
# characters (R, G, B, Y) and the user must repeat the sequence.
# Create a for loop that compares the two strings. For each match, add one
# point to user_score. Upon a mismatch, end the game.

user_score = 0
simon_pattern = 'RRGBRYYBGY'
user_pattern  = 'RRGBBRYBGY'

for i in range(len(simon_pattern)):
    if user_pattern[i] == simon_pattern[i]:
        user_score += 1
    else:
        break

print('User score:', user_score)




user_score = 0
first_pattern = 'RRGBRYYBGY'
second_pattern  = 'RRGBRYYBGY'

for i in range(len(first_pattern)):
    if first_pattern[i] == second_pattern[i]:
        print('Value of i:', i)
        print('First Pattern[i]:', first_pattern[i])
        print('Second Pattern[i]:', second_pattern[i])
        user_score += 1
        print('User Score:', user_score)
    else:
        break

print('Final User score:', user_score)





