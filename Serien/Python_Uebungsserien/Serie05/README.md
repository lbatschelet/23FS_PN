# Serie 05


> **Programmieren für Naturwissenschaften FS 2023**
> 
> Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet


## Aufgabe 1: Hello World

> Schreiben Sie ein Programm, welches folgende Ausgabe generiert (ersetzen Sie dabei [Ihr Name] mit Ihrem Namen):
> ```
> Hallo, mein Name ist [Ihr Name].
> Ich freue mich, Python zu lernen!
> ```
> Zusatzaufgabe: Schaffen Sie es, die zweizeilige Ausgabe mit einer einzigen print Anweisung zu erzeugen?

<details>
	<summary> Lösung anziegen</summary>

```python
print("Hallo unsere Namen sind Sofia, Florian und Lukas", "Wir freuen uns Python zu lernen!", sep="\n")
```

[Zum vollen Quellcode](S5A1.py)

</details>

## Aufgabe 2:

> - **a)** Begründen Sie, weshalb die folgenden zwei Kommentare nicht optimal sind:
>
> ```python
> print("Hallo") # gibt Hallo aus
> print("test") # muss später geändert werden
> ```

<details>
	<summary> Lösung anziegen </summary>
- `# gibt Hallo aus` gibt keine neue Information welche nicht sofort aus dem Programm klar wird.
- `# muss später geändert werden` erklärt nicht, was, wann, wo und weshalb etwas geändert werden muss.

</details>

> **b)** Welche Ausgabe erzeugen die folgenden zwei Anweisungen, wenn diese im Skript-Modus ausgeführt werden (Hinweis: `"\n"` repräsentiert das Zeilenumbruchzeichen)?
> ```python
> print("Hallo", "Python!", "Alles klar?", sep="\n", end=" ")
> print("Ja!")
> ```

<details>
	<summary> Lösung anziegen</summary>

```python
Hallo
Python!
Alles klar? Ja!
```

</details>


## Aufgabe 3: Rechnung

> Schreiben Sie ein Programm, das den arithmetischen Ausdruck $3 \cdot (2^5 +17)^2$ ausrechnet und das Resultat der Berechnung folgendermassen ausgibt:
> ```python
> 3 * (2^5 + 17)^2 = 7203
>```

<details>
	<summary> Lösung anziegen</summary>

```python
print("3 * (2^5 + 17)^2 =", end=" ")
print(3 * (2 ** 5 + 17) ** 2)
```

[Zum vollen Quellcode](S5A3.py)

</details>

Aufgabe 4:

	Zeile 1:
		a + b
		(a + b) + c
		((a + b) + c) + d
		(((a + b) + c) + d) + e
	Zeile 2:
		b * c
		d / e
		a + (b * c)
		(a + (b * c)) - (d / e)
	Zeile 3:
		b + c
		a / (b + c)
		d % e
		(a / (b + c)) - (d % e)
	Zeile 4:
		d - e
		c + (d - e)
		b * (c + (d - e))
		a / (b * (c + (d - e)))
	Zeile 5:
		b * c
		d / e
		(b * c) + (d / e)
		a + ((b * c) + (d / e))
		a = (a + ((b * c) + (d / e)))
	Zeile 6:
		d * e
		b + c
		(b + c) + (d * e)
		a = ((b + c) + (d * e))

Aufgabe 5:

Funktion range()

Die Funktion range() erstellt eine Liste von Werten in einem bestimmten Intervall

Die Werte können mit diesem Code angezeigt werden:

	for x in range():
		print(x)

range(5) Setzt eine Obergrenze, welche selber nicht mehr in den Werten vorkommt und erstellt bspw. folgende Werte:

	0
	1
	2
	3
	4

range(5, 10) setzt eine Untergrenze sowie eine obergrenze fest. Folgende Werte werden erstellt

	5
	6
	7
	8
	9

range(10, 21, 2) setzt neben der ober- und Untergrenze auch ein Step. Es werden folgende Werte erstellt

	10
	12
	14
	16
	18
	20


