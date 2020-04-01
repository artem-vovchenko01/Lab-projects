import numpy as np
import matplotlib.pyplot as plt
from math import *

rads = list(np.arange(-1*(2*pi), (2*np.pi), 0.01))

a = 4
b = 6
x = []
y = []

for fi in rads:
    x.append( a*fi - b*sin(fi) )
    y.append( a - b*cos(fi))

plt.plot(x, y)
plt.show()
