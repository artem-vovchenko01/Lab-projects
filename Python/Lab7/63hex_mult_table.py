import re

# Виведення 16-кової таблиці множення. Розрахунки в 10-ковій системі, далі
# виведення в 16-ковій за допомогою hex, str, re.sub()
for i in range(1,16):
    for k in range(1,9):
        num_i = re.sub( "0x", "", str(hex(i)) )
        num_k = re.sub( "0x", "", str(hex(k)) )
        num = str(hex(i*k))
        num = re.sub("0x",'',num)
        print(f"{num_k} * {num_i} = {num}\t",end = "")
    print()

print()

for i in range(1,16):
    for k in range(9,16):
        num_i = re.sub( "0x", "", str(hex(i)) )
        num_k = re.sub( "0x", "", str(hex(k)) )
        num = str(hex(i*k))
        num = re.sub("0x",'',num)
        print(f"{num_k} * {num_i} = {num}\t",end = "")
    print()
