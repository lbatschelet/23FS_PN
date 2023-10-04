counter = 0
total = 0

alter = int(input("Alter: "))
while alter > 0:
    total += alter
    counter += 1
    alter = int(input("Alter: "))

if counter == 0:
    counter = 1

average = total / counter
print("Durchschnittsalter der Studierenden: ", round(average, 2))
