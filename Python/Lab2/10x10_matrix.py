import numpy as np
import random

# Створення нульової матриці 10 на 10
a = np.zeros(shape = (10,10))

# Заповнюємо матрицю 10 на 10 випадковими числами
a[3,3] = 5
for row in range(0,10):
    for col in range(0,10):
        a[row,col] = random.randint(1,50)

print(a)
# Перетворюємо матрицю у вектор-рядок
a = a.ravel()
print(a)
