from math import pi, pow
from random import randint
from datetime import datetime
radius = randint(1,10)
area = pi * (pow(radius, 2))
now = datetime.now()
print(f"Radius is {radius}, area is {area:.2f}, timestamp: {now}")