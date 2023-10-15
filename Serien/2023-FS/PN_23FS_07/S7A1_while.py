"""
Programmieren für Naturwissenschaften
FS 2023
Serie: 7
Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet
Aufgabe: 1
"""

number = int(input("Geben Sie eine eine Natürliche Zahl ein: "))
produkt = 1
while number > 0:
    produkt *= number
    number -= 1
print("Fakultät dieser Zahl: ", produkt)
