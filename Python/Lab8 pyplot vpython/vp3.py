from vpython import *
import numpy
box_location = vector(0, -1.5, 0)
sphere_location = vector(0,0,0)

s = sphere(pos = sphere_location, radius = 1, color = color.red)
b = box(pos = box_location, size = vector(20, 1, 10), color = color.green)

time = 0
ls = list(numpy.arange(-3, 3, 0.01))
rev_ls = list(ls)
rev_ls.reverse()
sq = [i ** 2 for i in ls]
rev_sq = list(sq)
rev_sq.reverse()

# Movement of the center of the cube in parabolic manner
while True:
    for x, y in zip(ls, sq):
        rate(200)
        s.pos.x = x
        s.pos.y = y 
    for x, y in zip(rev_ls, rev_sq):
        rate(200)
        s.pos.x = x
        s.pos.y = y 
        