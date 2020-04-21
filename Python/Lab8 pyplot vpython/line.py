import numpy as np
import matplotlib.pyplot as plot
import math
plot.axes(projection='polar')

rads = list(np.arange(0.01, (2*np.pi), 0.01))

a = 1
coss = [ math.cos(ang) for ang in rads]
r = [ 2*a * (1 - cosf) for cosf in coss]

# Plot the graph
for radian, dis in zip(rads, r):
    plot.polar(radian,dis, "o")

# Display the Polar plot
plot.show()
