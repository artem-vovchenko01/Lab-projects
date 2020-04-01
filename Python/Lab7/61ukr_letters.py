with open("letters_60.txt",encoding="UTF-8") as f:
    text = f.read(60)

# Алфавіт
alphabet = "АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦШЩЬЮЯ"

numbers = []

# Визначаємо позиції українських букв у тексті
for i in range(len(text)):
    if text[i].upper() in alphabet:
        numbers.append(i)

string = " "*len(text)
# Пробіли під отриманими номерами замінюємо на _
for i in numbers:
    string = string[:i] + "_" + string[i+1:]

print(text)
print(string)
