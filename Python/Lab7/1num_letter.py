s = 0

# Визначаємо номер букви в алфавіті за допомогою ord()
for symbol in "SUM".lower():
    if 97 <= ord(symbol) <= 122:
        num = ord(symbol) -96
        s += num

print(s)
