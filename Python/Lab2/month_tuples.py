months = ["Грудень","Січнеь", "Лютий", "Березень", "Квітень", "Травень", "Червень", "Липень",\
    "Серпень", "Вересень", "Жовтень", "Листопад"]
ls = []
for i in range(0, len(months), 3):
    # Групуємо місяці в кортежі
    add = months[i], months[i+1],months[i+2]
    ls.append(add)
ls.insert(0,"Зима")
ls.insert(2,"Весна")
ls.insert(4,"Літо")
ls.insert(6,"Осінь")
print(tuple(ls))
