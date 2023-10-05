"""Musterlösung Serie 11, Aufgabe 1"""

import random
import matplotlib.pyplot as plt

def random_path(number):
    x_values = [0]
    y_values = [0]

    for i in range(number):
        x_rand = random.randint(-1,1) + x_values[i] #bei i geht auch -1
        y_rand = random.randint(-1,1) + y_values[i]

        x_values.append(x_rand)
        y_values.append(y_rand)

    plt.plot(x_values, y_values)
    plt.show()
random_path(100)


