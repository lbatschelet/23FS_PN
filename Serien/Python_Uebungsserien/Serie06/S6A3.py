"""
Programmieren für Naturwissenschaften
FS 2023
Serie: 6
Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet
Aufgabe: 3
"""

# Erstellen der Liste
numbers = (list(range(0,5,1)))
numbers.append(17)
numbers.insert(0, 99)
numbers[4] += 18
value = numbers[3]
print("Länge der Liste:", len(numbers))
numbers[1] = 1

print(numbers)
