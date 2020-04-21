"""
The module "currency" can return grammarly correct collocation with numbers and currency (dollar) name.
"""
def dollar (num):
    """
The "dollar" function is the main function of the "currency" module.
    """
    # Завершити програми, якщо не введено число
    try:
        num_int = int(num)
        # Відбираємо останній та два останніх символи введення
        last1 = num[len(num)-1]
        last2 = num[len(num)-2 : len(num)]
    except:
        print("Введіть число")
        quit()
    # Обираємо відмінок за лінгвістичними нормами (вкладені if - elif - else блоки)
    if last1 == "1":
        if last2 != "11":
            print(num_int, "долар")
        else: print(num_int, "доларів")
    elif last1 == "2" or last1 == "3" or last1 == "4":
        if last2 != "12" and last2 != "13" and last2 != "14":
            print(num_int, "долари")
        else:
            print(num_int, "доларів")
    else: print(num_int, "доларів")

a = input("Сума (в доларах): ")
# Виклик функції dollar. Виведення документації.
dollar(a)
print(__doc__)
print(dollar.__doc__)