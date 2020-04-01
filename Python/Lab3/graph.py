from matplotlib import pyplot as plt
from math import *
import numpy

# Уведення параметрів. Створення даних для осей.
a = int(input())
b = int(input())
dev_x = list(numpy.arange(0.1, 20, 0.001))
dev_y = list(map(lambda x: sin((a - b) / x), dev_x))
plt.plot(dev_x, dev_y)
plt.title(f"Function f(x) = sin( (A-B) / x ), A = {a}, B = {b}")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(1)
# Збереження у файл
plt.savefig("foo.png")
# Виведення графіка у вікні
plt.show()
