# Example Python Program to plot a polar plot of a circle

# import the numpy and pyplot modules
import numpy as np
import matplotlib.pyplot as plot
import math
plot.axes(projection='polar')

# Set the title of the polar plot
plot.title('Circle in polar format:r=R')

# Plot a circle with radius 2 using polar form
rads = list(np.arange(0.01, (2*np.pi), 0.01))
# r = 2a (1 - cosf)
a = 0.1
l = 0.1
coss = [ math.cos(ang) for ang in rads]
r = [ (a/cosf - l) for cosf in coss]
print(r)
for radian, dis in zip(rads, r):
    plot.polar(radian,dis, "o")

# Display the Polar plot
plot.show()