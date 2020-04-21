test = input()

# Цикл, який перевіряє кожні 2 сусідні символи з уведених
for i in range(0, len(test)):
    # Якщо символ - цифра, блок try визначить її парність. Якщо символ - блок
    # except співставить його з даним
    try:
        num = int(test[i])
        if num%2 == 0:
            print('+'*num)
        elif num%2 == 1:
            print("-"*num)
    except:
        if test[i] == "C":
            print("Comment")
