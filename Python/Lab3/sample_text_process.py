# Програма, що зчитує файл та виводить його на екран
file = open("Lab3/marfy.txt","r")
text = file.readlines()
file.close()
for line in text:
    print (line)
# Програма, що зчитує файл та виводить його на екран
file = open("Lab3/marfy.txt","r")
line = file.readline()
while line:
    print (line)
    line = file.readline()
file.close()
# Програма, що зчитує файл та виводить його на екран з доданою
# обробкою виняткових ситуацій
import sys
try:
    file = open("marfy.txt","r")
except IOError:
    print ("Не можна відкрити файл")
    sys.exit()
text = file.readlines()
file.close()
for line in text:
    print(line)
