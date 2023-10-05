# Serie 5
## Programmieren für Naturwissenschaften FS 2023
### Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet
### Aufgabe 1: 

S5A1.py

### Aufgabe 2:

	a)
	"# gibt Hallo aus" gibt keine neue Information welche nicht sofort aus dem Programm klar wird.

	"# muss später geändert werden" unklar, was wann geändert werden muss


	b)
	print("Hallo", "Python!", "Alles klar?", sep="\n", end=" ")
	print("Ja!")

	=>

	Hallo
	Python!
	Alles klar? Ja!

Aufgabe 3: 

S5A3.py

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


