"""Musterlösung Serie 11, Aufgabe 2"""

import pandas as pd

df = pd.read_csv("covid-data.csv")
"""print(df.columns)
print(df.head(4)) #erste 4 Elemente """
df_loc = df[["location", "new_cases", "new_deaths"]].groupby("location").sum()
print(df_loc)

#neue Spalte hinzufügen
df_loc["death_rate"] = df_loc["new_deaths"] / df_loc["new_cases"]
print(df_loc)

#zusatz

df_rate = df_loc.sort_values(by="death_rate", ascending= False)
print(df_rate.head(10))
print(df_rate)