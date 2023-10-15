import matplotlib.pyplot as plt
import random

def random_path(length):
    x = [0]
    y = [0]
    
    for _ in range(length):
        dx = random.randint(-1, 1)
        dy = random.randint(-1, 1)
        
        new_x = x[-1] + dx
        new_y = y[-1] + dy
        
        x.append(new_x)
        y.append(new_y)
        
    plt.plot(x, y)
    plt.xlabel('X-Koordinaten')
    plt.ylabel('Y-Koordinaten')
    plt.title('Zufälliger Pfad')
    plt.show()

# Beispielaufruf der Funktion mit einer Länge von 100
random_path(500)
