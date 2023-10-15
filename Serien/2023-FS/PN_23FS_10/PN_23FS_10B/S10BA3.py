# Wörterbuch zur Speicherung der Kundeninformationen
kunden_dict = {
    1: 'Samuel Meier',
    2: 'Hans Peterson',
    3: 'Klara Schmidt',
    4: 'Theresa Gerber'
}

# Funktion zur automatischen Generierung einer Kunden-ID
def generiere_kunden_id(kunden_dict):
    return max(kunden_dict.keys()) + 1

# Hauptprogramm
while True:
    name = input("Geben Sie den Namen des Kundes ein: ")
    
    # Überprüfung, ob der Kunde bereits im Wörterbuch ist
    if name in kunden_dict.values():
        kunde_id = [k for k, v in kunden_dict.items() if v == name][0]
        print(f"ID: {kunde_id}, Name: {name}")
    else:
        print("Dieser Kunde ist nicht registriert, möchten Sie ihn aufnehmen? (y/n)")
        antwort = input()
        if antwort.lower() == 'y':
            neue_id = generiere_kunden_id(kunden_dict)
            kunden_dict[neue_id] = name
            print(f"Kunde wurde hinzugefügt. ID: {neue_id}, Name: {name}")
    
    # Abfrage für weitere Eingabe
    weitere_abfrage = input("Weitere Abfrage? (y/n) ")
    if weitere_abfrage.lower() != 'y':
        break
