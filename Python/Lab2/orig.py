import numpy
import sys
# Програма, що створює візерунок в масиві NumPy
numpy.set_printoptions(threshold=sys.maxsize)
arr = numpy.zeros(shape=(21,21))
numpy.set_printoptions(linewidth=140)
while 1:
    for m in range(0,11,2):
        n = m
        c1 = 10
        c2 = 10
        x = 1 + m/2
        while c1 != 21-m:
            arr[n,c1] = x
            arr[n,c2] = x
            n+=1
            c1+=1
            c2-=1
        c1-=1
        c2+=1
        n-=1
        while c1 !=9:
            arr[n,c1] = x
            arr[n,c2] = x
            n+=1
            c1-=1
            c2+=1
    break
print(arr)
