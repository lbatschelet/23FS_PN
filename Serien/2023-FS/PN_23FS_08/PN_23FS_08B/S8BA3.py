import os
import csv
import statistics

# Pfad zum Ordner des aktuellen Skripts
script_dir = os.path.dirname(os.path.realpath(__file__))

# Eingabedateiname
input_file_name = "data.csv"

# Ausgabedateiname
results_file_name = "results.txt"

# Vollständiger Pfad zur Eingabedatei
input_file_path = os.path.join(script_dir, input_file_name)

# Vollständiger Pfad zur Ausgabedatei
results_file_path = os.path.join(script_dir, results_file_name)


# Einlesen der CSV-Datei
bevoelkerungsdaten = []

with open(input_file_path, 'r') as csvfile:
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
    
    # Vor 1980 liegen nur fünfjährlich die Daten vor. Daher muss das Wachstum in einem solchen Fall auf ein Jahr gemittelt werden.
    if jahr_aktuell < 1981:  
        wachstum = wachstum / (jahr_aktuell - jahr_vorher)  # Mittlere jährliche Veränderung
    
    if wachstum > max_wachstum:
        max_wachstum = wachstum
        jahr_max_wachstum = jahr_aktuell
        bemerkung = "(gemittelt über 5 Jahre)" if jahr_aktuell < 1980 else ""

# Ergebnisse in eine Textdatei schreiben
with open(results_file_path, 'w', encoding='utf-8') as f:
    f.write(f"Mittelwert der Bevoelkerung: {mittelwert}\n")
    f.write(f"Median der Bevoelkerung: {median}\n")
    f.write(f"Jahr mit dem grössten Bevoelkerungswachstum: {jahr_max_wachstum} {bemerkung}\n")

print("Die Ergebnisse wurden in results.txt geschrieben.")
