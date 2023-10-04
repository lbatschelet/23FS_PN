values = [6, 24, 3, 55, 3, 0]


#Aufgabe a
def indexierung(values):
    indizes = {}
    for i in values:
        indizes.update({i : values.index(i)})
    return indizes

print("Aufgabe a:", indexierung(values))

#Aufgabe b
def printer(values):
    for i in values:
        print(i)

print("Aufgabe b:")
printer(values)


#Aufgabe c
def erhoeher(values):
    for i in range(len(values)):
        values[i] += 1
    return values


print("Aufgabe c: ", erhoeher(values))

#Aufgabe d
def summarize(values):
    sum = 0
    for i in range(len(values)):
        sum += values[i]
    return sum
print(values)
print("Aufgabe d: ", summarize(values))
