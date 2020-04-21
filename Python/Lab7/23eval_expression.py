import random
numbers = input()
numbers = numbers.split(" ")
print(numbers)
row_to_eval = ""

# Конструюємо рядок для обчислення. Знаки + або - обираємо випадково
for i in range(0,len(numbers)):
    factor = random.randint(0,1)
    if factor == 0:
        sign = " - "
    else: sign = " + "
    if i == len(numbers) - 1:
        row_to_eval += numbers[i] + "."
        break
    row_to_eval += numbers[i] + sign

print(f"Що вираховуємо: {row_to_eval}")
print(f"Результат: {eval(row_to_eval)}")
