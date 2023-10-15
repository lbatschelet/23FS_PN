# Serie 9: Eigene Funktionen programmieren

> **Programmieren für Naturwissenschaften FS 2023**
> Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet

## Aufgabe 1: Kreisberechnung

> Schreiben Sie eine Funktion, welche über einen formalen Parameter verfügt, welcher dem Radius eines Kreises entspricht. Die Funktion soll die Fläche und den Umfang des Kreises berechnen und die Berechnungen dann mit Hilfe des Schlüsselworts `return` zurückgeben. Rufen Sie die Funktion danach 3-mal mit je einem anderen tatsächlichen Parameter auf und speichern Sie die Rückgabewerte der Funktion in zwei Listen, um diese dann mit Hilfe der Funktion `print` auszugeben.
>
> **Tipp:** Wenn Sie nicht wissen, wie Sie in einer Funktion mehrere Werte zurückgeben können, betrachten Sie Beispiel 76 im Skript auf Seite 102


## Aufgabe 2: Funktionsparameter

> Schreiben Sie eine Funktion `greet`, welche bis zu drei Parameter akzeptiert, jedoch mindestens einen Parameter benötigt, nämlich den Namen einer Person. Unten finden Sie einige Beispiele, welche Ausgaben die Funktion generieren sollten. Passen Sie Ihre Funktion so an, dass die Beispiele in Tabelle 1 funktionieren. Falls Sie Hilfe brauchen, schauen Sie sich Beispiel 73 auf Seite 94 im Skript an
> 
> | Funktionsaufruf                        | Ausgabe                                                              |
> | -------------------------------------- | -------------------------------------------------------------------- |
> | `greet("Monika")`                      | `Hallo Monika!`<br>`Guten Morgen!`<br>`Es ist 20 Grad draussen.`       |
> | `greet("Sepp", "Wie geht's denn so?")` | `Hallo Sepp!`<br>`Wie geht's denn so?`<br>`Es ist 20 Grad draussen.` |
> | `greet("Hans", temp=10)`               | `Hallo Hans!`<br>`Guten Morgen!`<br>`Es ist 10 Grad draussen.`       |
> 
> Tabelle 1: Ihre Funktion sollte dieselben Ausgaben generieren, wie in dieser Tabelle dargestellt.


## Aufgabe 3: Funktionen auslagern

> Betrachten Sie das untenstehendes Programm. Sie werden bemerken, dass das Programm verschiedene Verantwortungen übernimmt. Ihre Aufgabe ist es, die einzelnen Verantwortungen zu identifizieren und für jede Verantwortung je eine Funktion zu definieren und den Code entsprechend auszulagern. Rufen Sie danach Ihre Funktionen in der richtigen Reihenfolge auf – verwenden Sie wo sinnvoll Parameter und Rückgaben.

```python
ages = []
done = False

while not done:
    user_input = int(input("Alter eingeben: (-1 zum Beenden): "))
    if user_input == -1:
        done = True
    else:
        ages.append(user_input)

print("Alle Alter aufsteigend sortiert:")
ages.sort()
for i in range(len(ages)):
    print("Alter von Student", i, ages[i])

import statistics
print("Mittelwert der Alter: ", round(statistics.mean(ages), 2))
```
