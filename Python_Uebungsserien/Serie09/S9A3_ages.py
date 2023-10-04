"""
Programmieren für Naturwissenschaften
FS 2023
Serie: 9
Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet
S9A3_ages.py
"""


import statistics

def age_list():
    ages = []
    done = False

    while not done:
        user_input = int(input("Alter eingeben (-1 zum Beenden): "))
        if user_input == -1:
            done = True

        else:
            ages.append(user_input)
    return ages

def sort_and_print(list):
    print("Alle Alter aufsteigend sortiert:")
    list.sort()
    for i in range(len(list)):
        print("Alter von Student:in", i + 1, list[i])

def mean_and_print(list1):
    mean = statistics.mean(list1)
    print("Durchschnittsalter:", round(mean, 2))
    
