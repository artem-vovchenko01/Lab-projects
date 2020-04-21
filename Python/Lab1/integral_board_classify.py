num = input("Кількість електронних елементів ІС: ")

try:
    num = int(num)
except:
    print("Помилка введення")
    quit()


if num >= 10000:
    print("Надвелика, НВІС")
elif num >= 1000:
    print("Велика, ВІС")
elif num >= 100:
    print("Середня, СІС")
elif num in range(1,100):
    print("Мала, МІС")
else:
    print("Помилка введення")
