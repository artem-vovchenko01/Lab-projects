from vpython import *
import numpy
new_box = box(pos = vector(0,0,0), size = vector(20,20,20), color = color.green)
sph = sphere(pos = vector(0,0,0), radius = 1, color = color.blue)
x = []
y = []
sph.trail = curve(color= sph.color)
# Rules desired direction by equation
for num in numpy.arange(0,10, 0.01):
    x.append(num)
    y.append(-1*num + 10)

for num in numpy.arange(10, 0, -0.01):
    x.append(num)
    y.append(num - 10)

for num in numpy.arange(0, -10, -0.01):
    x.append(num)
    y.append(-1*num - 10)

for num in numpy.arange(-10,0,0.01):
    x.append(num)
    y.append(num + 10)

# Sphere's center movement
while True:
    for ex, vay in zip(x, y):
        rate(500)
        sph.pos.x = ex
        sph.pos.y = vay
        sph.trail.append(pos = (sph.pos))