import numpy
# Введення аргументів
try:
    x = int(input("Коефіцієнт перед x: "))
    y = int(input("Коефіцієнт перед y: "))
    b = int(input("Вільний член 1: "))
    x1 = int(input("Коефіцієнт перед x1: "))
    y1 = int(input("Коефіцієнт перед y1: "))
    b1 = int(input("Вільний член 2: "))
except:
    print("Уведіть лише числа.")
    quit()

# Створення масивів
args = numpy.array( [[x,y],[x1,y1]] )
nums = numpy.array( [b, b1] )

print("Система:")
print(x,"* x","+",y,"* y", "=", b)
print(x1,"* x","+",y1,"* y", "=", b1)

# Розв'язання системи рівнянь. Виведення помилки при LinALgError
try:
    res = numpy.linalg.solve(args, nums)
    print("Результат: ", res)
except:
    print("Input error")
