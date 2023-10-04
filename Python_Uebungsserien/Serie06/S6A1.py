"""
Programmieren für Naturwissenschaften
FS 2023
Serie: 6
Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet
Aufgabe: 1
"""

a, b = 2, 2
c = 4

d = a + b * c
c *= c % a
e = d / a + c
f = e // b

print(a, b, c, d, e, f, sep="\n")