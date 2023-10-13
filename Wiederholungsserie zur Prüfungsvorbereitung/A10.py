import random

counter = [0, 0, 0, 0, 0, 0]

for i in range(1, 101):
    wurf = random.randint(1, 6)
    counter[wurf - 1] += 1

print(counter)