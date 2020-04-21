import re
import numpy
for x in numpy.arange(-1,2.1,0.1):
    y = x**2 -1
    x = round(x,3)
    y = round(y,3)
    plot = int(round(y*20))
    add = " "*(plot+30)
    if x <= 0: suffix = " "
    else: suffix = "  "
    to_print = str(x) + suffix + add + "*" + " "*30
    if to_print[9] == " ":
        to_print = to_print[:35] + "|" + to_print[36:]
    print(to_print)
