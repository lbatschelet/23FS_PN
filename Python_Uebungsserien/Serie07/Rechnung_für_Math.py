import numpy as np
from scipy.optimize import minimize_scalar

def f(x):
    return 0.5 * np.sin(x) + 2

def df(x):
    return 0.5 * np.cos(x)

t1 = 1
t2 = 4
avg_slope = (f(t2) - f(t1)) / (t2 - t1)

def objective(x):
    return (df(x) - avg_slope) ** 2

result = minimize_scalar(objective, bounds=(t1, t2), method='bounded')
t0 = result.x

print(f"t_0: {t0}")
