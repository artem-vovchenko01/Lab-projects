import re
from string import ascii_lowercase
from collections import Counter

f =  open("Lab3/marfy.txt","r") 
text = f.read()
x = re.compile(r"\D")
symbols = re.findall(x,text)
text = str()
for symbol in symbols:
    text += symbol
# Визначаємо кількість різних букв
c = Counter(letter for line in text for letter in line.lower() if letter in ascii_lowercase)
words = text.split()
# Визначаємо частоту появи слів
c1 = Counter(one_word for one_word in words)
print("Частота появи букв: ",c)
print("Частота появи слів: ",c1)
# Визначаємо кількість операторів циклів
c2 = Counter(one_word for one_word in words if one_word in ["for","while"])
print("Кількість операторів циклів: ",c2)
