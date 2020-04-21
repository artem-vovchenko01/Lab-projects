raw = input()
dig = raw[0]
try:
    test = int(dig)
except:
    print("First must be a number. ")
    quit()

def find_next(dig):
    """
    Визначаємо наступну цифру
    """
    if 0 <= int(dig) <=8:
        next_dig = int(dig) + 1
    else: next_dig = 0
    return next_dig

print(find_next(dig))
