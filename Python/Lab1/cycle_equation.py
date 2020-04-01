#1.2.2.5
import math
x_beg = 13.3
x_fin = 14.5
a = 7.32
b = 0.15

# порожній список
x_list = []

# Перебір усіх можливих за умовою варіантів x і додавання їх до списку
while x_beg <= x_fin:
    x_list.append(x_beg)
    # Визначення кроку змінної і округлення результату
    x_beg = round(x_beg + 0.15, 3)

# Обчислення і виведення результатів
for x in x_list:
    y = math.sqrt( math.fabs(a + math.sin(b)) ) * (x**2)
    print(y)
