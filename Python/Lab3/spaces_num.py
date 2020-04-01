import re
f_name = "marfy.txt"
# Відкриваємо файл для читання
f = open(f"{f_name}", encoding="utf-8")
text = f.readlines()
count = 0
# Створюємо шаблон для пошуку співпадінь
pattern = re.compile(r" ")
for line in text:
    # Пошук співпадінь
    x = re.findall(pattern, line)
    if 0 <= len(x) <= 1:
        count += 1
        print(f"Рядок, що підходить:\"{line}\"")
print(f"Кількість рядків, що мають 0 або 1 пробіл у файлі {f_name}: {count}")