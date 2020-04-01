import re
words = "hello   hi  good   banana hahaha  boolean  fine   how  fine      you  so much fine   you  i."
# Відокремлюємо слова
pattern = re.compile(r"\w+")
word_list = re.findall(pattern, words)
unique = []
for i in range(0, len(word_list) - 1):
    el = word_list[i]
    first_let = el[0]
    last_let = el[-1]
    word_list[i] = first_let + re.sub(
        first_let, "", el[1:]
    )  # Видаляємо подальші входження першої літери
    el = word_list[i]
    word_list[i] = (
        re.sub(last_let, "", el[:-1]) + last_let
    )  # Видаляємо попередні входження останньої літери
    el = word_list[i]
    # Залишаємо лише перші входження кожної літери
    for k in range(0, len(el)):
        try:
            if el[k] not in unique:
                unique.append(el[k])
            else:
                word_list[i] = el[:k] + el[k + 1 :]
                el = word_list[i]
        except:
            break
    unique = []
    # У словах з непарною к-стю літер видаляємо середню
    if len(el) % 2 == 1:
        middle = len(el) // 2 + 1
        word_list[i] = el[:middle] + el[middle + 1 :]
        el = word_list[i]

    word_list[i] = el[1:] + el[0]  # Перенесемо першу літеру в кінець слова
    el = word_list[i]
    word_list[i] = el[-1] + el[0:-1]  # Перенесемо останню літеру на початок слова
    el = word_list[i]
    word_list[i] = el[1:-1]  # Видалимо першу і останню літери
    el = word_list[i]

print("Результуючий список слів: ")
print(word_list)

not_equal = ""
# Друк відповідних слів в один рядок
for i in word_list:
    if i != word_list[-1] and len(i) > 0:
        not_equal = f"{not_equal} {i}"

print("Слова, які не співпадають з останнім словом в результаті перетворень: ")
print(not_equal)
