# Порожні списки кодів ASCII та символів, що відповідають заданим ASCII кодам
ord_list = []
chr_list = []

# Заповнення списку символами з кодами з діапазону 96..127 включно
for i in range(96, 128):
    chr_list.append(chr(i))

# Заповнення списку кодами відповідних латинських літер
for i in range(ord('a'), ord('z')+1):
    ord_list.append(i)

print("СИМВОЛИ З ЗАДАНОГО ДІАПАЗОНУ: ")
print(chr_list)

print("КОДИ СИМВОЛІВ ЛАТИНСЬКОГО АЛФАВІТУ: ")
print(ord_list)
