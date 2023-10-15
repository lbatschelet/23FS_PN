# Schreiben Sie ein Programm, welches nach zwei Zahlen x und y fragt.
# Berechnen Sie mit diesen Werten die folgende Formel:
# e + \frac{\sqrt{x + sin(\frac{\pi}{2})}}{y - exp(x^2)}

import math

# Eingabe
x = float(input("Bitte geben Sie eine Zahl für x ein: "))
y = float(input("Bitte geben Sie eine Zahl für y ein: "))

# Berechnung
e = math.e
pi = math.pi
ergebnis = e + math.sqrt(x + math.sin(pi/2)) / (y - math.exp(x**2))

# Ausgabe
print("Ergebnis:", math.floor(ergebnis))
