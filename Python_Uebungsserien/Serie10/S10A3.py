import math

cubes = {}

for i in range(100, 10001):
    cubes[i] = math.pow(i, 3)

zahl = int(input("Ganze Zahl eingeben: "))

print("Kubikzahl ihrer Zahl: {:'}".format(cubes.get(zahl)))
