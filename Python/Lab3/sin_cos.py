import math

# Виведення таблиць синусів, косинусів, експонент непарних чисел від 1 до 30
for i in range(1,30,2):
    print('sin(%d) = %f'.ljust(20)%(i,math.sin(i)), end='')
    print('cos(%d) = %f'.ljust(20)%(i,math.cos(i)), end = "")
    print("exp(%d) = %d".ljust(20)%(i,math.exp(i)))
