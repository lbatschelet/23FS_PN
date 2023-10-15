# Gegebene Mengen von Tieren und Fleischfressern
animals = {'rabbit', 'tiger', 'dog', 'bird', 'cat', 'zebra', 'koalas'}
carnivores = {'tiger', 'dog', 'bird', 'cat', 'shark'}

# Aktualisieren der 'animals' Menge mit neuen Tieren
animals.update(['elephant', 'deer', 'shark', 'giraffe', 'cat'])

# Entfernen von 'koalas' aus der 'animals' Menge
animals.discard('koalas')

# Ausgabe der endgültigen 'animals' Menge
print("Animals:", animals)

# Ausgabe der Differenz zwischen 'animals' und 'carnivores'
print("Difference:", animals.difference(carnivores))
