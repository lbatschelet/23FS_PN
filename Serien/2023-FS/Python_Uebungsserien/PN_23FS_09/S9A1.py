"""
Programmieren für Naturwissenschaften
FS 2023
Serie: 9
Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet
S9A1_main.py
"""

import math

def circle(rad=0):
    area = math.pow(rad, 2) * math.pi
    circumference = rad * 2 * math.pi
    return area, circumference

radien = []
flaechen = []
umfange = []

loop = "y"
while loop == "y":
    rad = float(input("Geben Sie den Radius eines Kreises ein: "))
    area, circumference = circle(rad)
    radien.append(round(rad, 2))
    flaechen.append(round(area, 2))
    umfange.append(round(circumference, 2))
    print("Radius:", rad)
    print("Fläche: ", area)
    print("Umfang: ", circumference)
    loop = input("Wollen Sie noch einen weiteren Kreis berechnen? (y/n)")

print("Radien: ", radien)
print("Flächen: ", flaechen)
print("Umfänge: ", umfange)
