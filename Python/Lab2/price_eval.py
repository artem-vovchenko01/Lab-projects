# Список товарів
ls = [["Хліб", "10", "20"],["Суп","30","2"],["М'ясо","40","5"],["Картопля","25","10"],["Кава","5","30"]]
text = []
order = []
price = 0
# Динамічне (список товарів можна змінювати) виведення доступних товарів
def txt():
    for i in range(0,len(ls)):
        text.append(  str(i+1) +" - "+ ls[i][0] + " " + "(" + ls[i][1] + "грн / од" + ")")
# Розрахунок ціни, друк замовлення
def processing (inp, num):
    global price, ls
    app = ls[inp-1][0], num
    order.append( app )
    price += int(ls[inp-1][1]) * num
    new_num = int(ls[inp-1][2]) -num
    ls[inp-1][2] = str(new_num)

txt()
# Цикл, що приймає замовлення, обробляє правильність уведених даних.
while 1:
    choice = input( "Оберіть замовлення: " + str(text) + " ")
    try:
        a = int(choice)
        if not 0 < a <= len(ls):
            print("Invalid value.")
            break
    except: 
        print("Input error.")
        break

    num = input("скільки одиниць товару бажаєте? " + ls[int(choice)-1][2] + " доступно: ")
    try:
        a = int(num)
        if not 0 < int(num) <= int(ls[int(choice)-1][2]):
            print("Invalid value.")
            break
    except:
        print("Input error")
        break
    processing(int(choice),int(num))

    q = input("Бажаєте ще щось?  yes / no: ")
    if q == 'no': break
    elif q != "yes":
        print("Input error.")
        break
    print(order)
    print("Поточна сума: " + str(price) + " грн.")

# Результат
print("До сплати: " + str(price) + " грн.")