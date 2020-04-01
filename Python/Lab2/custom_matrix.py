import numpy
m = numpy.fromfunction(lambda x,y: x == y , (100,100))

for row in range(0,100):
    for col in range(0,100):
        if m[row][col] == "True":
            m[row][col] = 1

print(m)