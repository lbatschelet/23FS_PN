import os
import pandas as pd

# Pfad zum Ordner des aktuellen Skripts
script_dir = os.path.dirname(os.path.realpath(__file__))

# Dateiname
file_name = "covid-data.csv"

# Vollständiger Pfad zur Datei
file_path = os.path.join(script_dir, file_name)

# Datei mit Pandas lesen
df = pd.read_csv(file_path)
print("Erste 5 Zeilen der Tabelle:")
print(df.head())
print("Spalten in der Tabelle:")
print(df.columns)

# 2. Totale Fälle und Todesfälle für jede Ortschaft
grouped_data = df.groupby('location').agg({
    'total_cases': 'last',
    'total_deaths': 'last'
}).reset_index()

print("Totale Fälle und Todesfälle für jede Ortschaft:")
print(grouped_data)

# 3. Todesrate berechnen und als neue Spalte hinzufügen
grouped_data['death_rate'] = (grouped_data['total_deaths'] / grouped_data['total_cases']) * 100

print("Tabelle mit Todesrate:")
print(grouped_data)

# 4. Die 10 Länder mit den höchsten Todesraten
top_death_rates = grouped_data.sort_values(by='death_rate', ascending=False).head(10)
print("Die 10 Länder mit den höchsten Todesraten:")
print(top_death_rates)
