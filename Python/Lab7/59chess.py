import math, re
inp = input("Уведіть позицію коня у форматі [буква][цифра]: ")
letter_dict = {}
letters = "ABCDEFGH"
for i in range(1,9):
    letter_dict[letters[i-1]] = i
try:
    let = re.search(r"\w",inp)
    num = re.search(r"\d",inp)
    y = letter_dict[let.group().upper()]
    x = int(num.group())
except:
    print("Incorrect input.")
    quit()

# Створюємо матрицю для порожньої шахової дошки
line = [0,0,0,0,0,0,0,0]
matrix = []
for i in range(1,9):
    matrix.append(line)

# Встановлюємо коня на позицію, вказану у введенні 
insert = [0,0,0,0,0,0,0,0]
insert[y-1] = 1
matrix[x-1] = insert

# Створення списку з доступними ходами для коня
steps = []
x_list = []
y_list = []
for i in [1,2,-1,-2]:
    x_list.append(x+i)
    y_list.append(y+i)
for j in x_list:
    for k in y_list:
        if 0 < j < 9 and 0 < k < 9 and math.fabs(j-x) != math.fabs(k-y):
            steps.append([j,k])

# Заміна значень, що відповідають ходам коня, у клітинках шахової дошки на зірочку
for i in range(0,len(steps)):
    x_insert = steps[i][0] - 1
    y_insert = steps[i][1] - 1
    insert = list(matrix[x_insert])
    insert[y_insert] = "*"
    matrix[x_insert] = insert

# Псевдографічне виведення
for i in range(0,8):
    print("-"*56)
    for k in range(0,8):
        if k == 0:
            print("|",end="")
        to_print = f" {matrix[i][k]}{' '*2}|{' '*2}"
        print(to_print,end= "")
        if k == 7:
            print(f"    {i+1}",end="")
    print()
    if i == 7:
        print("-"*56)
        p = " "*6
        print()
        print(f"  A{p}B{p}C{p}D{p}E{p}F{p}G{p}H{p}")