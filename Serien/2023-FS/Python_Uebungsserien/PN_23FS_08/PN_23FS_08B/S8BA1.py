# Path: S8BA1.py
# Schreiben Sie ein Programm, welches 100 zufällige ganze Zahlen zwischen -200 und 200 erstellt
# (**Tipp:** Verwenden Sie einen Loop). Geben 5 von diesen zufällig generierten Zahlen aus.

import random

# Liste zum Speichern der zufälligen Zahlen
zufallszahlen = []

# 100 zufällige Zahlen generieren
for i in range(100):
    zufallszahl = random.randint(-200, 200)
    zufallszahlen.append(zufallszahl)

# 5 zufällige Zahlen aus der Liste ausgeben
ausgewaehlte_zahlen = random.sample(zufallszahlen, 5)
print("5 zufällig ausgewählte Zahlen:", ausgewaehlte_zahlen)
