import math

x = 7
y = 4.5
z = 3.249

# Обчислення виразу за допомогою імпортованої бібліотеки math
a = math.atan(z+y) + math.sqrt(z**2 - y) + math.fabs(x)

# Виведення результату
print(a)