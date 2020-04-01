import numpy
# Створення масиву з числами від 1.0 да 100.0
a = numpy.arange(1.0,101.0)
# Змінюємо розміри на 10 на 10
a = a.reshape(10,10)
print(a)
