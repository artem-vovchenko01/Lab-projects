import random
# Створення порожніх списків, опис умови
r_list = []
negative_list = []
bigger_list = []
range_list = []
def_num = 20
range_set = range(-40, 41)

# Заповнення списку випадковими числами із діапазону
for x in range(1, 101):
    r_list.append(random.randint(-100,101))

# Заповнення списків знайденими випадковими числами за даними критеріями
for x in r_list:
    if x < 0:
        negative_list.append(x)
    if x > def_num:
        bigger_list.append(x)
    if x in range_set:
        range_list.append(x)

# Виведення результатів
print("INITIAL SET: ")
print(r_list)
print("NEGATIVE NUMBERS: ")
print(negative_list)
print("BIGGER THAN",str(def_num)+":")
print(bigger_list)
print("IN THE KNOWN RANGE (FROM", range_set[0],"to",str(  range_set[len(range_set)-1]  )+")")
print(range_list)
