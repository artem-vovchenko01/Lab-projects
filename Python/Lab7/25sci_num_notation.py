import math
x = -0.0486


power = 0
# Приводимо число до стандартного вигляду (1 < x < 10, і рахуємо степінь, до якого піднести
# x, щоб отримати дане число)
while math.fabs(x) < 1:
    x *= 10
    power -= 1

while math.fabs(x) > 10:
    x /= 10
    power += 1

print(f"{x}E{power}")
