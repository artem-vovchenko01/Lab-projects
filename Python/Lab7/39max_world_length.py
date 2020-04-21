row = "Yet another row to figure out the longest word in the world ( hmm, not exactly )"
words = row.split(" ")
# Визначаємо найдовше слово, використовуючи lambda, map і ф-ю max
max_length = max(map(lambda x: len(x),words))
print(f"Довжина найбільшого слова: {max_length}")
