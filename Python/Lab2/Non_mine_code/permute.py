import numpy as np
# Функція генерує випадкові числа від 0 до n-1 включно
def permute(n):
    arr = np.random.permutation(n)
    print(arr)

permute(50)