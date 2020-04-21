import array
# Введення даних, розбиття їх на списки з числами.
ls1 = input("Type numbers separated by space for array 1: ")
ls2 = input("Type numbers separated by space for array 2: ")
ls1 = ls1.split()
ls2 = ls2.split()

ls_arr1 = []
ls_arr2 = []

# Перетворення введених даних у тип int і розміщення їх у списку.
try:
    for i in range(0, len(ls1)):
        ls_arr1.append(int(ls1[i]))
    for i in range(0, len(ls2)):
        ls_arr2.append(int(ls2[i]))
except:
    print("Масиви мають містити тільки числа. ")
    quit()

# Створення масивів.
arr1 = array.array("i", ls_arr1)
arr2 = array.array("i", ls_arr2)

print("Масив 1:", arr1)
print("Масив 2:",arr2)

def compare (A, B):
    """
    Функція порівнює два масиви. Вважає їх схожими, якщо у обох масивах використані одні й ті ж символи.
    Сигналізує про помилку, якщо хоча б один з масивів порожній.
    """
    err = ''
    if len(A) == 0 or len(B) == 0:
        print("Заповніть обидва масиви. ")
        quit()

    # Перевірка масивів на однаковість.
    if A == B: print("Масиви однакові. "); quit()

    # Сортування
    A = sorted(A)
    B = sorted(B)

    # Наступні цикли по порядку вибирають елементи масива А і перевіряють, чи є хоча б один такий же
    # елемент у масиві В. На основі цього робиться висновок про схожість чи несхожість масивів.
    for i in range(0, len(A)):
        sym = A[i]
        count = B.count(sym)
        if count == 0:
            err = "Масиви несхожі."
            break
    for i in range(0, len(B)):
        sym = B[i]
        count = A.count(sym)
        if count == 0:
            err = "Масиви несхожі."
            break
    if len(err) == 0:
        print('Масиви схожі.')
    else:
        print(err)

# Виклик функції
compare(arr1, arr2)