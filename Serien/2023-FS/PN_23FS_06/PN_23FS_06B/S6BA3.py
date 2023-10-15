"""
Programmieren für Naturwissenschaften
FS 2023
Serie: 6B
Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet
Aufgabe: 3
"""
import math

radius = float(input("Geben Sie den Radius ein: "))

area = radius ** 2 * math.pi
scope = radius * 2 * math.pi

print("\n")
print("________________")
print("Radius =", radius)
print("Fläche =", round(area, 2))
print("Umfang =", round(scope, 2))
