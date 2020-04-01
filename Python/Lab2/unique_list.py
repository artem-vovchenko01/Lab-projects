text = input("Уведіть рядок: ")
text2 = input("Уведіть рядок 2: ")
# Заповнюємо списки словами із введення
l1 = text.split()
l2 = text2.split()

unique = []

# Унікальні елементи додаємо до відповідного списку
for i in range(0, len(l1)):
    item = l1[i]
    if l2.count(item) == 0:
        unique.append(item)
for i in range(0,len(l2)):
    item = l2[i]
    if l1.count(item) == 0:
        unique.append(item)
print(unique)
