#1.2.2.1

counter = 1

# 5 спроб для введення - оператор for
for coutner in range(5):
    inp = input()
    counter+=1
    # Якщо вводиться число 5, зпохвалити і авершити програму
    if inp == "5":
        print("Чудовий вибір!")
        break

