import array
# Введення даних, розбиття їх на список із числами.
ls1 = input("Type numbers separated by space for array: ")
ls1 = ls1.split()

ls_arr1 = []

# Перетворення введених даних у тип int і розміщення їх у списку.
try:
    for i in range(0, len(ls1)):
        ls_arr1.append(int(ls1[i]))
except:
    print("Масив має містити тільки числа. ")
    quit()

# Створення масиву.
arr1 = array.array("i", ls_arr1)

print("Даний масив:", arr1)

def find (A):
    """
    Функція приймає масив, перевіряє кожен його елемент.
    Якщо к-сть таких же елементів, як і поточний, більше від половини всії елементів, то він є переважним.
    Інакше масив не має переважного елемента, як і у випадку, коли він порожній.
    """
    for i in range(0, len(A)):
        sym = A[i]
        count = A.count(sym)
        if count > len(A) / 2:
            print("Масив має переважний елемент", sym)
            return
    print("Масив не має переважного елементу.")

# Виклик функції
find(arr1)