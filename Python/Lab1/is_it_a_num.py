#1.2.1.7
test = input()
try:
    result = int(test)
except:
    print("Помилка введення")
    quit()

if result in range(0, 10):
    print("Тип введення: ", type(test))
    print("Тип результату: ", type(result))
else:
    print("Помилка введення")