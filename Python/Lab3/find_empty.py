import re
f_name = "Lab3/marfy.txt"
# Відкриваємо файл для читання
f = open(f"{f_name}",encoding="UTF-8")
text = f.readlines()
count = 0
# Створюємо шаблон для пошуку співпадінь
pattern = re.compile(r"\n")
for line in text:
    # Пошук співпадінь
    x = re.match(pattern,line)
    if x:
        count += 1
print(f"Кількість порожніх рядків у файлі {f_name}: {count}")
