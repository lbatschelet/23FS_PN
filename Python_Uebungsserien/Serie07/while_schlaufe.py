
loop = "y"
while loop == "y":
    number = int(input("Geben Sie eine Zahl ein: "))

    produkt = 1

    while number > 0:
        produkt *= number
        number -= 1
    print(produkt)
    loop = input("Wollen Sie eine weitere Zahl eingeben? (y/n)")