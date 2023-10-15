# Serie 8B: Standardmodule verwenden

> **Programmieren für Naturwissenschaften FS 2023**
> Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet

## Aufgabe 1: Standardmodul `random`

> Schreiben Sie ein Programm, welches 100 zufällige ganze Zahlen zwischen -200 und 200 erstellt
> (**Tipp:** Verwenden Sie einen Loop). Geben Sie 5 von diesen zufällig generierten Zahlen aus.

<details>
    <summary> Mögliche Lösung anzeigen </summary>

```python
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
```

[Vollstängier Quellcode](S8BA1.py)

</details>

## Aufgabe 2: Standardmodul `math`

> Schreiben Sie ein Programm, welches nach zwei Zahlen x und y fragt. Berechnen Sie mit diesen Werten die folgende Formel:
>
> ![Funktion](PN_23FS_08B/RESOURCES/funktion_A2.png)
> 
> Geben Sie das Resultat abgerundet aus.

<details>
    <summary> Mögliche Lösung anzeigen </summary>

```python
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
```

[Vollstängier Quellcode](S8BA2.py)

</details>

## Aufgabe 3: Standardmodul `statistics`

> Auf Ilias finden Sie eine Datei `data.csv`. Die Zahlen geben den jährlichen Bevölkerungsstand von 1941 bis 2021 der Stadt Bern an[^1]. Schreiben Sie ein Programm, welches die Datei einliest und danach folgende Aufgaben erfüllt:
>
> - Berechnen Sie den Mittelwert und den Median des Bevölkerungsstandes über alle Jahre hinweg mit dem Modul `statistics`. **Tipp:** Entfernen Sie den Leerschlag innerhalb der Zahlen (130 688 → 130688).
> - Geben Sie das Jahr an, in welchem das grösste Bevölkerungswachstum beobachtet werden kann hat im Vergleich zum Vorjahr.
> - Schreiben Sie Ihre Ergebnisse in eine Textdatei `results.txt`.

[^1]: Quelle: https://www.bern.ch/themen/stadt-recht-und-politik/bern-in-zahlen/katost/01bev

<details>
    <summary> Mögliche Lösung anzeigen </summary>

```python
import csv
import statistics

# Einlesen der CSV-Datei
bevoelkerungsdaten = []

with open('data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=';')
    next(csvreader)  # Überspringe die Kopfzeile
    for row in csvreader:
        if len(row) == 2:
            jahr, bevoelkerung = row
            bevoelkerung = int(bevoelkerung.replace(" ", ""))
            bevoelkerungsdaten.append((jahr, bevoelkerung))
        else:
            print(f"Warnung: Ungültige Zeile übersprungen: {row}")

# Mittelwert und Median berechnen
bevoelkerungszahlen = [bevoelkerung for jahr, bevoelkerung in bevoelkerungsdaten]
mittelwert = statistics.mean(bevoelkerungszahlen)
median = statistics.median(bevoelkerungszahlen)

# Grösstes Bevölkerungswachstum finden
max_wachstum = 0
jahr_max_wachstum = None
bemerkung = ""

for i in range(1, len(bevoelkerungsdaten)):
    jahr_aktuell = int(bevoelkerungsdaten[i][0])
    jahr_vorher = int(bevoelkerungsdaten[i - 1][0])
    
    wachstum = bevoelkerungsdaten[i][1] - bevoelkerungsdaten[i - 1][1]
    
    # Vor 1980 liegen nur fünfjährlich die Daten vor. 
    # Daher muss das Wachstum in einem solchen Fall auf ein Jahr gemittelt werden.
    if jahr_aktuell < 1981:  
        wachstum = wachstum / (jahr_aktuell - jahr_vorher)  # Mittlere jährliche Veränderung
    
    if wachstum > max_wachstum:
        max_wachstum = wachstum
        jahr_max_wachstum = jahr_aktuell
        bemerkung = "(gemittelt über 5 Jahre)" if jahr_aktuell < 1980 else ""

# Ergebnisse in eine Textdatei schreiben
with open('results.txt', 'w') as f:
    f.write(f"Mittelwert der Bevoelkerung: {mittelwert}\n")
    f.write(f"Median der Bevoelkerung: {median}\n")
    f.write(f"Jahr mit dem grössten Bevoelkerungswachstum: {jahr_max_wachstum} {bemerkung}\n")

print("Die Ergebnisse wurden in results.txt geschrieben.")
```

- [Vollstängier Quellcode](S8BA3.py)
- [CSV-Datei](data.csv)
- [Ausgabedatei](results.txt)


</details>


