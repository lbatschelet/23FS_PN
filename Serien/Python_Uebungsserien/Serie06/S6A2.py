"""
Programmieren für Naturwissenschaften
FS 2023
Serie: 6
Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet
Aufgabe: 2
"""

points_max = int(input("Maximal erreichbare Punkte: "))

# Schlaufe um mehrere Noten zu berechnen
while True:
    points = int(input("Erreichte Punkte: "))

    # Vorgehen falls eingegebene Punktzahl die maximale Punktzahl überschreitet.
    while points > points_max:
        # Nachfragen ob mit dem zu hohen Wert weitergearbeitet werden soll, oder ob der Wert korrigiert werden soll
        proceed = input(
            "Warnung: Die erreichte Punktzahl ist höher als die maximale Punktzahl. Möchten Sie die erreichten Punkte korrigieren? (Ja/Nein)")
        if proceed.lower() == "ja":
            points = int(input("Bitte korrigieren Sie die erreichten Punkte: "))
        else:
            break
    # Notenberechnung
    grade = (points / points_max) * 5 + 1

    round(grade, 3)
    print("\n",)
    print("_______________")
    print("Maximale Punkte:", points_max)
    print("Erreichte Punkte:", points)
    print("Note:", grade)

    repeat = input("Möchten Sie eine weitere Note berechnen? (Ja/Nein)")
    if repeat.lower() == "nein":
        break
