from vpython import *
from math import *

box_location = vector(0, 0, 0)
scene.center = vector(0, 0, 0)
scene.title = "Rotate"
b = box(pos = box_location, size = vector(5, 5, 5), color = color.green)

# Rotate the scene to make an effect of cube rotation
while True:
    rate(50)
    scene.forward = scene.forward.rotate(angle=0.095,axis=scene.up)
    