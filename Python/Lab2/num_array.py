import numpy as np

a = np.array( list(map(lambda x: round(float(x),1), range(1,100))) )
print(a)

b = 7 
print(a.itemsize)
c = np.array([(1,2,4),(4,5,6)])
dd = np.array([(4,3,5),(4,2,5)])
print(c.dtype)
#print(a.ndin)
print(c.size)
print(c.shape)
print(c)
print(c.reshape(3,2))
print(c[0:,1])
print( np.linspace(1,500, 200))
d = np.array(range(1,100000))
print(d)
print(d.max())
print(d.min())
print(d.sum())
print(c.sum(axis=0))
print(c.sum(axis=1))
print(np.sqrt(c))
print(np.vstack((c,dd)))
print(np.hstack((c,dd)))
print(c.ravel())
import matplotlib.pyplot as plt

x = np.arange(0, 3*np.pi, 0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()