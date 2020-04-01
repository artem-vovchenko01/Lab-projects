from vpython import *
import numpy
my_ball = sphere(pos = vector(0,0,0), radius = 5)
surf = box(pos = vector(0, -57,0), size = vector(30, 10, 30), color = color.red)

g = 9.8
t = list(numpy.arange(0, 1, 0.01))
d = [ ((g * tm) ** 2) / 2 for tm in t ]
down = list(d)
d.reverse()
up = list(d)
initial = int(my_ball.pos.y)

# Changing sphere's position by formula s = (gt^2) / 2
while True:
    for shift in down:
        rate(100)
        my_ball.pos.y = initial - shift
    for shift in up:
        rate(100)
        my_ball.pos.y = initial - shift
