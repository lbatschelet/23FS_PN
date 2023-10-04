import numpy
import matplotlib.pyplot
from scipy.optimize import curve_fit
import random

# Definition der Funktion
def f(x, a, b, c):
    return a * numpy.exp(-b * x) + c

# Erzeugen der x-Daten
xdata = numpy.arange(0, 4, 0.1)

# Erzeugen der y-Daten
ydata = f(xdata, 2.5, 1.3, 0.5) + numpy.random.uniform(-0.1, 0.1, len(xdata))

# Durchführen der Kurvenanpassung
popt, pcov = curve_fit(f, xdata, ydata)

# Plotten der Daten
matplotlib.pyplot.plot(xdata, ydata, 'o', label='data')

# Plotten der fit-Funktion
matplotlib.pyplot.plot(xdata, f(xdata, *popt), label='fit')

# Hinzufügen einer Legende
matplotlib.pyplot.legend()

# Anzeigen des Plots
matplotlib.pyplot.show()
