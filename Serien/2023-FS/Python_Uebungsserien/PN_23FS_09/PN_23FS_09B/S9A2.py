
import random as rnd

# Aufgabe 5: Funktion fragt nach dem Bereich für die Zufallszahl
def ask_range():
    start = input("Bitte gib den Anfang des Bereichs ein (Standard ist 1): ")
    end = input("Bitte gib das Ende des Bereichs ein (Standard ist 100): ")
    return int(start) if start.isnumeric() else 1, int(end) if end.isnumeric() else 100

# Aufgabe 2: Die Funktion fragt den Spieler nach einer Eingabe und überprüft, ob es eine Zahl ist.
def askguess():
    while True:
        guess = input("Bitte gib eine Zahl ein: ")
        if guess.isnumeric():
            return int(guess)
        else:
            print("Das war keine Zahl. Bitte versuche es erneut.")

# Aufgabe 3: Die Funktion überprüft, ob die geratene Zahl größer, kleiner oder gleich der gesuchten Zahl ist.
def validateguess(guess, n):
    h, l, c = 0, 0, 0
    if guess > n:
        h = 1
    elif guess < n:
        l = 1
    else:
        c = 1
    return h, l, c


print("Willkommen zum Zahlenraten!")
print("Du hast 10 Versuche, um die gesuchte Zahl zu erraten.")

# Aufgabe 5: Fragen nach dem Bereich für die Zufallszahl
start, end = ask_range()

# Aufgabe 1: Eine Zufallszahl zwischen start und end wird generiert.
n = rnd.randint(start, end)

# Zusatz Aufgabe: Maximale Anzahl an Versuchen
max_attempts = 10
attempts = 0

# Start des Spielcodes
over = False
while not over and attempts < max_attempts:
    # Aufgabe 2
    guess = askguess()
    attempts += 1
    # Aufgabe 3
    h, l, c = validateguess(guess, n)

    # Überprüfung der Werte h, l, c
    assert h + l + c == 1
    assert h >= 0
    assert l >= 0
    assert c >= 0

    # Aufgabe 4: User-Feedback basierend auf den Werten h, l, c
    if h:
        print("Deine Schätzung war zu hoch! Versuch es erneut.")
    elif l:
        print("Deine Schätzung war zu niedrig! Versuch es erneut.")
    else:
        print("Richtig geraten! Das Spiel ist beendet.")
        over = True

# Zusatz Aufgabe: Spiel verloren, falls maximale Anzahl an Versuchen erreicht ist
if not over:
    print(f"Das Spiel ist verloren. Die gesuchte Zahl war {n}.")

