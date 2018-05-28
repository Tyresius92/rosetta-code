import random

lst = []

for i in range(1, 10):
    lst.append(i)

print(lst)

random.shuffle(lst)

score = 0

while sorted(lst) != lst:
    print(lst)
    print("How many digits from the left would you like to reverse?")

    index = int(input())

    lst[:index] = reversed(lst[:index])
    score += 1

print("Well done! Your final score was: " + str(score))
