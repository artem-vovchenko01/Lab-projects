import re,math
numbers = input("Уведіть менше 50 чисел: ")
find_del = input("Число, яке треба видалити: ")
target = input("Яке число замінити? ")
new = input("На яке замінити? ")

# Записуємо і зчитуємо файл
with open("numbers.txt","w") as f:
    f.write(numbers)
with open("numbers.txt") as f:
    text = f.read()

# Пошук чисел за допомогою регулярних виразів
pattern = re.compile(r"[+-]?\d+")
nums_list = re.findall(pattern,text)

mx = None
pos_count = 0
zero_count = 0
neg_count = 0
for i in range(0,len(nums_list)):
    num = int(nums_list[i])
    if i == 0:
        mx = num
    elif math.fabs(num ) > mx:
        mx = num
    if num > 0:
        pos_count += 1
    if num == 0:
        zero_count += 1
    if num < 0:
        neg_count += 1

print(f"Початковий файл: {text}")
print(f"Найбільше число за модулем: {mx}")
print(f"Кількість додатніх чисел: {pos_count}")
print(f"Кількість від'ємних чисел: {neg_count}")
print(f"Кількість нулів: {zero_count}")
text1 = re.sub(str(find_del),"",text)
text2 = re.sub(target,new,text)
print(f"Результуючий файл після видалення обраного: {text1}")
print(f"Результуючий файл після заміни: {text2}")
