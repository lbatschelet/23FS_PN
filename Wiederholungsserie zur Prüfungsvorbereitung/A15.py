full = False
counter = 0
MAX = 10

while True:
    if not full and counter < MAX:
        counter += 3
    else:
        counter = 0
        break

#b

i = 10
while i >= 0:
    print(i)
    i -= 2

for i in range(10, -1, -2):
    print(i)

#c
import random

values = random.sample(range(-100, 100), 20) # erstellen einer Liste mit 20 zufälligen Werten 
pos = []
neg = []

for i in range(len(values)):
    if values[i] >= 0:
        pos.append(values[i])
    else:
        neg.append(values[i])

print(values)
print(pos)
print(neg)

#d

import random

values = random.sample(range(-100, 100), 20)  # Erstellen einer Liste mit 20 zufälligen Werten
total = 0
threshold = 100
index = 0

while total < threshold and index < len(values):
    total += values[index]
    index += 1
print(total)
