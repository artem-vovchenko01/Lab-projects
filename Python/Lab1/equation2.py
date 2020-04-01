#1.2.1.9
import math

a = 14.2
b1 = 10.2
b2 = 2.78
c = 6.43

# В залежності від значення b порівняно з c, вибрати одну з гілок рівняння.
# Надрукувати 2 різних вихідних результати.
if b1 > c:
    num = math.sin(a+b1)**2
    denom = math.sqrt(math.fabs(b1+c))
    x1 = 1 + num / denom
    print(x1)

if b2 <= c:
    x2 = c*math.sqrt(a*b2 + math.sin(c))
    print(x2)