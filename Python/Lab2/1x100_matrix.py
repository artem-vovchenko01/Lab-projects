import numpy as np, random

# Створення нульової матриці 1 на 100. Заповнення її випадковими числами
a = np.zeros(shape = (1,100))
for i in range(0,100):
    a[0,i] = random.randint(1,100)
print(a)

# Зміна форми на 100 на 1
a = a.reshape(100,1)
print(a)
