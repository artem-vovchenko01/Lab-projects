import re
f_name = "marfy.txt"
# Відкриваємо файл для читання
f = open(f"{f_name}",encoding="utf-8")
text = f.read()
# Створюємо шаблони для пошуку співпадінь
pattern1 = re.compile(r"[13579][2468]")
matches1 = pattern1.finditer(text)
pattern2 = re.compile(r"[^\d\W][\W\d]\d+")
matches2 = pattern2.finditer(text)
pattern3 = re.compile(r"\b[A-Z]\w*\b")
matches3 = pattern3.finditer(text)
pattern4 = re.compile(r"yes", re.I)
matches4 = pattern4.finditer(text)
pattern5 = re.compile(r"(ні ?)+")
matches5 = pattern5.finditer(text)
pattern6 = re.compile(r"\d{1,2}\.\d{1,2}\.\d{2}")
matches6 = pattern6.finditer(text)
pattern7 = re.compile(r"[\(\),\.+\"\'!\:;\?]")
matches7 = pattern7.finditer(text)
# Виведення результатів
print("Непарна - парна цифра: ")
for match in matches1:
    print(match)
print("Буква - не буква - число: ")
for match in matches2:
    print(match)
print("Слово, що починається з великої літери: ")
for match in matches3:
    print(match)
print("Слово yes з виористанням довільного регістру: ")
for match in matches4:
    print(match)
print("Слово 'ні' >= 1 разів: ")
for match in matches5:
    print(match)
print("Дата формату d(d).d(d).dd: ")
for match in matches6:
    print(match)
print("Знак пунктуації: ")
for match in matches7:
    print(match)