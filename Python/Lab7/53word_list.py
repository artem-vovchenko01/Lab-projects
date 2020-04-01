import re
words = "hello,hi,good,fine,how,fine,you,so,much,fine,you,i."
# Відокремлюємо слова
pattern = re.compile(r"\w+")
word_list = re.findall(pattern,words)
# Реалізація зворотного пороядку за допомогою зрізу
print(f"Дана послідовність слів у зворотному порядку: {word_list[::-1]}")

first = []
last = []
unique = []
only_once = list(word_list)
ent_count = {}
alphabet = []

for i in range(0,len(word_list)):
    elem = word_list[i]
    # Кількість входжень запишемо у словник
    try:
        num = ent_count[elem]
        ent_count[elem] = num + 1
    except:
        ent_count[elem] = 1

    if i == 0:
        first.append(elem)
        last.append(elem)
        unique.append(elem)
        alphabet.append(elem)
        continue
    # Реалізація завдань по алфавітному сортуванню, використовуючи вбудоване порівняння рядків
    fact = True
    if elem > alphabet[-1]:
        alphabet.append(elem)
        fact = False
    elif i == 0:
        alphabet.insert(-1,elem)
        fact = False
    if fact == True:
        for x in alphabet[::-1]:
            if elem > x:
                ind = alphabet.index(x)
                alphabet.insert(ind+1,elem)
                break
            if x == alphabet[0]:
                alphabet.insert(0,elem)
    for k in first:
        if elem > first[-1]:
            first.append(elem)
        if elem < last[-1]:
            last.append(elem)
    # Видалення елементів, що повторюються
    if elem not in unique:
        unique.append(elem)
    else:
        only_once.remove(elem)
        alphabet.remove(elem)
        try:
            only_once.remove(elem)
        except:
            pass
        try:
            num_ind = alphabet.index[elem]
            alphabet[num_ind+1:].index[elem]
            alphabet.remove(elem)
        except:
            pass

print(f"Слова, перед якими йдуть лише слова, що стоять за алфавітом раніше: {first}")
print(f"Слова, перед якими йдуть лише слова, що стоять за алфавітом пізніше: {last}")
print(f"Список, у якому слова не повторюються: {unique}")
print(f"Список з усіма словами, що зустрічаються лише 1 раз: {only_once}")
print(f"Кількість входжень різних елементів у рядок: {ent_count}")
print(f"Список зі слів в алфавітному порядку: {alphabet}")
