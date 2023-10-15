import random as rnd

# TODO: Aufgabe 2: Ihre Implementation der Funktion askguess:
def



# TODO: Aufgabe 3: Ihre Implementation für die Funktion validateguess:
def



# TODO: Aufgabe 1: Zufallszahl für die gesuchte Zahl
n =

## Start des Spielcodes:
over = False
while not over:
    guess = askguess() #Siehe Aufgabe 2
    h, l, c = validateguess(guess, n) # Siehe Aufgabe 3

    ## Folgender Code überprüft ob Sie die Werte h, l, c richtig gesetzt haben. Sollte ein Fehler auftreten so können
    # Sie die Fehlermeldung nutzen um mögliche logische Fehler bei Ihrer Implementation aus Aufgabe 3 zu überprüfen.
    # Hinweis: Ein Ausbleiben von Fehlermeldungen heisst nicht, dass der Code wie gewünscht funktioniert.
    assert h + l + c == 1
    assert h >= 0
    assert l >= 0
    assert c >= 0
    ##

    # TODO: Aufgabe 4: Geben Sie userfeedback basierend auf den Werten h, l, c:



    # Ende des Spielcodes

