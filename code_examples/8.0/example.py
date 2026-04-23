# math module examples
import math
print(math.sqrt(4))
print(math.ceil(3.1))
print(math.pow(2,3))

# random module examples
from random import random, randint
print(random())
print(randint(1,26))

# datetime module examples
from datetime import datetime as dt
now = dt.now()
print(now)
print(now.strftime("%m/%d/%Y"))