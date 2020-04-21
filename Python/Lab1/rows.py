string1 = "This is the test string. "
string2 = "This is a second string"
print("Початковий рядок: " + string1)

# Переконуємося, що змінювати рядки поелементно неможливо.
# Виконається блок except, бо в блоці try помилка
try:
    string1[0] = 't'
except:
    print("Змінювати рядки поелементно неможливо")

# Розмноження рядка + об'єднання
res_string = string1*10 + string2
print("Об'днання 2-х рядків та розмноження рядка: " + res_string)

# Виведення рядків, що відрізняються на 1 символ за допомогою зрізів
ch_symbol = string1[:3] + "S" + string1[4:]
print("Рядок зі зміненим символом: " + ch_symbol)
add_symbol = string1[:4] + "!" + string1[4:]
print("Рядок із доданим символом: "+ add_symbol)
