another = "y"
lst = []

while another == "y":
    lst.append(input("Geben Sie eine Zahl der Liste hinzu: "))
    another = input("Wollen Sie eine weitere Zahl hinzufügen? (y/n)")

def maxima(values):
    maximas = []
    for i in range(1, len(values) -1):
        if values[i] > values[i - 1] and values[i] > values[i + 1]:
            maximas.append(values[i])
    return maximas

print(maxima(lst))

