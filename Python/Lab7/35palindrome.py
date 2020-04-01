import re
word = input("Придумайте паліндром: ")
find = re.search(r"\w+",word)
word = find.group().lower()
# Визначимо чи є слово паліндромом за допомогою зрізу рядка у зворотньому порядку
if word == word[::-1]:
    print("Так, це паліндром!")
else:
    print("Це не паліндром")
    