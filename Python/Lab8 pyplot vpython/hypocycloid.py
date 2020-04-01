import numpy as np
import matplotlib.pyplot as plt
from math import *
rads = list(np.arange(0.01, (2*np.pi), 0.01))
a = 8
b = 2
x = []
y = []
for fi in rads:
    x.append( (a+b)*cos(fi) - b*cos( ((a+b)/b)*fi ))  
    y.append( (a+b)*sin(fi) - b*sin( ((a+b)/b) * fi ))

plt.plot(x, y)
plt.show()
