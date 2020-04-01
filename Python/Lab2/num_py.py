import numpy

# Шукаємо детермінант заданої матриці: 1*5 - (-2*4)

arr = numpy.array([(1,-2),(4, 5)])
#arr = numpy.array( [ (2,1), (6,3) ] )
if numpy.linalg.det(arr) != 0:
    d = numpy.linalg.det(arr)
    print(arr)
    print("Детермінант: ", d)
else:
    print("Детермінант = 0. ")
    quit()


# Розв'язуємо систему рівнянь x + 2y = 1.1; 0x + y = 0.5
# Обробляємо ситуацію Singular Matrix

a = numpy.array( [ [1.0, 2.0], [0.0, 1.0] ] )
b = numpy.array( [1.1, 0.5] )

x = numpy.linalg.solve(a,b)
print("Результат: ", x)

print("Перевірка: ", numpy.dot(a,x)-b)

