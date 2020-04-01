from vpython import *
from math import *

box_location = vector(-20, 0, 0)
sphere_location = vector(20,0 , 0)

s = sphere(pos = sphere_location, radius = 1.5, color = color.red)
b = box(pos = box_location, size = vector(5, 3, 1), color = color.green)
s.color = color.cyan

collision = False
dx = 0.01
while True:
    rate(500)
    if collision == False:
        s.pos.x -= dx
        b.pos.x += dx
    if collision == True:
        s.pos.x += dx
        b.pos.x -= dx
    if s.pos.x - b.pos.x <= 4:
        collision = True
    if s.pos.x - b.pos.x > 40:
        collision = False
