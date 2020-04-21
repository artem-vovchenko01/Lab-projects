names = ["Nick","Peter","Sam","Josh"]
print(names)
try:
    num = int(input("Say Hello to somebody! (type index number): ")) - 1
except:
    print("Please, enter an integer. ")
# Обробка ситуації IndexError
try:
    print(f"Hello {names[num]}!")
except IndexError:
    print("Your choice is out of list's range. ")
