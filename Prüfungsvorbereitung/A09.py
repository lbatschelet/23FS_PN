import random

another = "y"

while another == "y":
    zahl_1 = random.randint(0, 2)
    zahl_2 = random.randint(0, 2)
    zahl_3 = random.randint(0, 2)
    print(zahl_1, zahl_2, zahl_3)
    if zahl_1 == zahl_2 and zahl_1 == zahl_3:
        print("Gratulation! Sie haben den grossen Preis gewonnen! Gehen Sie Lotto spielen!")
    elif zahl_1 == zahl_2 or zahl_1 == zahl_3 or zahl_2 == zahl_3:
        print("Gratulation! Sie haben den kleinen Preis gewonnen!")
    else:
        print("Scchade! Viel Erfolg beim nächsten Versuch!")
    another = input("Wollen Sie weiterspielen? (y/n)")