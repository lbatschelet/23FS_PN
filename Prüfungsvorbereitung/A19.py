"""# (a)
for i in list(range(1, 1000 + 1)):
    do_something(i)

# (b)
import random
while len(values) > 0:
    values.pop(random.randint(0, len(values) - 1)) # -1 damit Grenze nicht unterschritten wird

# (c)
wort = "Urs"
for i in range(len(wort)):
    print(f"{i} : {wort[i]}")
"""
# (d)
values = [1, 1]
while len(values) < 100:
    values.append(values[-1] + values[-2])

print(values)