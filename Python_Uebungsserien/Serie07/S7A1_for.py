"""
Programmieren für Naturwissenschaften
FS 2023
Serie: 7
Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet
Aufgabe: 1
"""

number = int(input("Geben Sie eine natürliche Zahl ein: "))
produkt = 1
for i in range(1, number+1):
    produkt *= i

print("Fakultät dieser Zahl: ", produkt  )
