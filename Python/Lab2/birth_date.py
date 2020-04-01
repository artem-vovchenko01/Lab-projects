data = ( ["Семенов Андрій Миколайович","07.12.1975"],["Петренко Василь Іванович","16.05.1984"], ["Бондарчук Дмитро Васильович","21.10.1969"],["Левченко Максим Юрійович","12.04.2001"],["Зубко Марина Віталіївна","15.12.1975"])
def reorder():
    """
    Функція змінює порядок у списку з датами для правильного сортування
    """
    for i in range(0,len(split_date)):
        p = split_date[i].pop(1)
        split_date[i].insert(0, p)
        p = split_date[i].pop(2)
        split_date[i].insert(0,p)

split_date = []
merged = []
final = []
# Розділяємо дату на окремі елементи - дні, місяці, роки для подальших операцій
for i in range(0,len(data)):
    ls = data[i][1].split('.')
    split_date.append(ls)
reorder()
split_date = sorted(split_date)
reorder()
# Згортаємо дати в один елемент у сортованому списку
for i in range(0,len(split_date)):
    s = '.'.join(split_date[i])
    merged.append(s)
# Заповнюємо фінальний список у правильному порядку
for i in range(0,len(merged)):
    chck = merged[i]
    for i in range(0,len(data)):
        if data[i][1] == chck:
            final.append(data[i])
print(tuple(final))

