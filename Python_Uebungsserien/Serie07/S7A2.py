"""
Programmieren für Naturwissenschaften
FS 2023
Serie: 7
Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet
Aufgabe: 2
"""
another = "y"
while another == "y" or another == "Y":
    alter_summe = 0
    count = 0
    print("Dieses Programm rechnet ihnen das Durchschnittsalter einer Gruppe aus. Geben sie das alter der Personen einzeln ein. Beenden können Sie das Programm mit der Eingabe 0")
    alter_neu = int(input("Geben Sie das Alter eines Studierenden oder einer Studierenden ein: "))
    while alter_neu > 0:
        count += 1
        alter_summe += alter_neu
        alter_neu = int(input("Geben Sie das Alter eines Studierenden oder einer Studierenden ein: "))


    alter_durchscnitt = alter_summe / count

    print("Durchschnittsalter: ", round(alter_durchscnitt, 2))
    another = input("Möchten Sie ein weiteres Durchschnittsalter berechnen? (y/n)")