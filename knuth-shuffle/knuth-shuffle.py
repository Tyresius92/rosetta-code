import random

ray = []

for i in range(25):
    ray.append(i)

print(ray)

for i in range(len(ray)):
    index = random.randint(i, len(ray) - 1)
    ray[i], ray[index] = ray[index], ray[i]

print(ray)
