"""
Programmieren für Naturwissenschaften
FS 2023
Serie: 8
Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet
Aufgabe: 3
"""

import statistics

import os

# Pfad zum Ordner des aktuellen Skripts
script_dir = os.path.dirname(os.path.realpath(__file__))

# Dateiname
file_name = "passagierfrequenz.csv"

# Vollständiger Pfad zur Datei
file_path = os.path.join(script_dir, file_name)

# Datei lesen
with open(file_path, "r") as file:
    content = file.read()
    print(content)


# leere listen für die werte aus der Datei erstellen
dtv_values = []
dwv_values = []
dnwv_values = []
name_values = []

with open(file_path, "r") as file:
    # Die erste Zeile lesen (Header)
    header_line = file.readline()
    # Header-Zeile am Komma aufteilen
    header = header_line.split(';')

    # Den Index der gewünschten Spalten finden
    dtv_index = header.index("DTV")
    dwv_index = header.index("DWV")
    dnwv_index = header.index("DNWV")
    name_index = header.index("Bahnhof_Haltestelle")


    # Zeilen lesen
    for line in file:
        # Zeilen am Komma aufteilen
        row = line.strip().split(';')
        # Werte in die entsprechende Liste einfügen
        dtv_values.append(float(row[dtv_index]))
        dwv_values.append(float(row[dwv_index]))
        dnwv_values.append(float(row[dnwv_index]))
        name_values.append(row[name_index])
    # Stationen mit maximaler und minimaler Frequenz finden
        # grösste Werte in der Liste suchen
        max_dtv = max(dtv_values)
        min_dtv = min(dtv_values)
        # index dieser Werte suchen
        max_index = dtv_values.index(max_dtv)
        min_index = dtv_values.index(min_dtv)
        # stationsname mit hilfe des index festlegen
        name_max = name_values[max_index]
        name_min = name_values[min_index]

dtv_mean = statistics.mean(dtv_values)
dwv_mean = statistics.mean(dwv_values)
dnwv_mean = statistics.mean(dnwv_values)
dtv_median = statistics.median(dtv_values)
dwv_median = statistics.median(dwv_values)
dnwv_median = statistics.median(dnwv_values)

print("DTV \t= Durchschnittlicher täglicher Verkehr (Montag bis Sonntag)")
print("DWV \t= Durchschnittlicher werktäglicher Verkehr (Montag bis Freitag)")
print("DNWV \t= Durchschnittlicher nicht-werktäglicher Verkehr (Samstage, Sonntage, Feiertage)")
print("__________________________________________________")
print("Durchschnittswerte:")
print("\t DTV pro Bahnhof (2018): \t", round(dtv_mean, 2))
print("\t DWV pro Bahnhof (2018): \t", round(dwv_mean, 2))
print("\t DNWV pro Bahnhof (2018): \t", round(dnwv_mean, 2))
print("Median:")
print("\t DTV pro Bahnhof (2018): \t", round(dtv_median, 2))
print("\t DWV pro Bahnhof (2018): \t", round(dwv_median, 2))
print("\t DNWV pro Bahnhof (2018): \t", round(dnwv_median, 2))
print("__________________________________________________")
print(name_max, "ist die Station mit dem höchsten DTV, und zwar: \t", max_dtv)
print(name_min, "ist die Station mit dem geringsten DTV, und zwar: \t", min_dtv)
