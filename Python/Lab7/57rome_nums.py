# Usage of Rome numbers:
# 10 - X, 50 - L, 100 - C, 500 - D, 1000 - M
with open("rome_nums.txt") as f:
    input = f.read()

# Словник з відповідністю римських цифр арабським числам
conversion = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

# Рахуємо кількість входень цифр у число
counts = dict(conversion)
for i in "IVXLCDM":
    counts[i] = 0

# Переводимо введення в набір десяткових чисел
converted = []
for number in input:
    converted.append(conversion[number])
    counts[number] += 1

# Виключаємо очікувані помилки
for i in "IXC":
    if counts[i] > 3:
        print("More than triple repeat of I/X/C not allowed.")
        quit()
for i in "VLD":
    if counts[i] > 1:
        print("More than triple repeat of I/X/C not allowed.")
        quit()
if "VX" in input:
    print("VX is not allowed.")
    quit()
for i in range(1, len(converted)):
    if converted[i] > converted[i - 1] and (converted[i - 1] in [5, 50, 500]):
        print("Write V/L/D on the left side of bigger number is not allowed.")
        quit()
if "MMMMM" in input:
    print("Numbers only up to 4999 allowed.")


queue = [0]
result = 0

# Робота з чергою чисел для обрахунку результату відповідно до правил
for i in range(0, len(converted)):
    if i == 0:
        queue.append(converted[i])
        continue
    if converted[i] <= queue[-1]:
        queue.append(converted[i])
    if converted[i] > queue[-1]:
        result += converted[i] - queue[-1] + sum(queue[:-1])
        queue = [0]

    if i == len(converted) - 1 and len(queue) != 0:
        result += sum(queue)
        queue = [0]

print(f"Римське число {input} в арабській системі числення: {result}")
