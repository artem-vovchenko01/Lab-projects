#1.2.2.4
lucky = 7

number = -1
# Постійно запрошувати число, допоки користувач не вгадає число або не відмовиться продовжувати
while True:
    number = input("Введіть щасливе число: ")
    # Перевести введені дані в int, якщо це можливо
    try:
        number = int(number)
    except:
        number = str(number)
    # Привітати і завершити програму при успішному введенні
    if number == lucky:
        print("Ви вгадали!")
        quit()
    answer = input("Do you want to continue using this program? ")
    # Завершити програму, якщо користувач вводить no
    if answer == "no":
     quit()

