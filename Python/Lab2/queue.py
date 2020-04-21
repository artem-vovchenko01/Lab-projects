import array
# Створення порожнього масиву.
q = array.array("i")

def add():
    """
    Ця функція додає елемент до масиву.
    """
    global q
    new = input("Print new number to the queue: ")
    try:
        new = int(new)
        q.append(new)
        q = sorted(q)
    except:
        print("Incorrect value.")
        quit()
    print(q)

def remove():
    """
        Ця функція видаляє елемент з масиву, якщо такий є.
    """
    global q
    rem = input("Print the number to remove: ")
    try:
        rem = int(rem)
    except:
        print("Incorrect value.")
    try:
        q.remove(rem)
        q = sorted(q)
    except:
        print("There is no such value. Nothing changed. ")

    print(q)

def check():
    """
        Ця функція перевіряє наявність елемента в масиві. Якщо наявний - видає його позицію
        у масиві (починаючи з 1)
    """
    global q
    chck = input("Print number to check: ")
    try:
        chck = int(chck)
        count = q.count(chck)
    except:
        print("Incorrect value")
        quit()
    if len(q) == 0:
        print("The array is empty.")
    elif count == 0:
        print("There is no such number in queue.")
    else:
        print("The position in queue: ", q.index(chck) + 1)

def inp():
    """
        Ця функція обробляє інтерактивну взаємодію з користувачем.
    """
    while 1:
        question = input("Choose what to do: a - append, r - remove, c - check: ")
        if question == "a":
            add()
        elif question == "r":
            remove()
        elif question == "c":
            check()
        else: 
            print("Incorrect value.")
            quit()
        factor = input("Do you want to continue? y/n ")
        if factor == "y":
            continue
        elif factor == "n":
            break
        else:
            print("Incorrect value.")
            break

# Виклик головної функції
inp()
