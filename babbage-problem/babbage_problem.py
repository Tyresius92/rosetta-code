from math import sqrt

GOAL_END = 269696

mod_number = 10 ** len(str(GOAL_END))

n = 2   # GOAL_END is even, so odd numbers need not be considered

while ((n ** 2) % mod_number) != GOAL_END:
    n += 2
    if n % 1000000 == 0:
        print("made it to " + str(n))

print(str(n) + " is the lowest value whose square ends in " + str(GOAL_END))
print(str(n) + "^2 is equal to " + str(n ** 2))
