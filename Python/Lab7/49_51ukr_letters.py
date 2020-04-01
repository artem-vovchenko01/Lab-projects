text = "Так! Бути українській мові в середовищі програмістів!."
# Виконаємо завдання за допомогою ф-ї upper()
print(text[:-1].upper())
# Означимо алфавіт
alphabet = "абвгдеєжзиіїйклмнопрстуфхцчшщьюя"
to_order = {}
fetched = []
for i in range(0,len(text)):
# Якщо буква не було просканована та вона є в алфавіті (тут це означатиме і те, що вона є малою, що вимагається умовою), зафіксуємо її номер в алфавіті і додамо до словника, щоб потім з його допомогою отримати необхідний порядок.
    if text[i] not in fetched and text[i] in alphabet:
        index = alphabet.index(text[i])
        to_order[index] = text[i]
        fetched.append(text[i])
# Отримуємо список наявних ключів (номери використаних букв)
order = list(to_order.keys())
order = sorted(order)
# Отримуємо атрибути словника у необхідному порядку, додаємо до списку
ordered = []
for i in order:
    ordered.append(to_order[i])
print("Список використаних у рядку малих літер за алфавітом: ")
print(ordered)

