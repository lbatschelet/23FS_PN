"""
Programmieren für Naturwissenschaften
FS 2023
Serie: 9
Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet
S9A1_main.py
"""

from S9A1_calc_circle import circle

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
