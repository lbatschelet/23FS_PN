"""
Programmieren für Naturwissenschaften
FS 2023
Serie: 9
Gruppe: Sofia Kessler, Florian Mohaupt, Lukas Batschelet
S9A1_calc_circle.py
"""

import math

def circle(rad=0):
    area = math.pow(rad, 2) * math.pi
    circumference = rad * 2 * math.pi
    return area, circumference
