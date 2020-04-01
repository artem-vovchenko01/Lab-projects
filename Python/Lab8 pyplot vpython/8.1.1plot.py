from matplotlib import pyplot as plt
import numpy as np
import math

# Списки точок для побудови
x = list(np.arange(0.1,2,0.05))
sqr = [z ** 2 for z in x]
qub = [z **3 for z in x]
exp = [2 ** z for z in x]
log = [math.log(z, 10) for z in x]
y = list(x)

# Побудова
plt.plot(x, sqr,label = "quadratic")
plt.plot(x, qub, label = "qubic")
plt.plot(x, y, label = "linear")
plt.plot(x, exp, label = "exponential (2^x)")
plt.plot(x, log, label = "logarithm (log2(x))")
plt.legend()
plt.show()
