import random, re
def baseAnytoAny(k,num,n):
    """ Конвертація з систем числення, що використовують тільки цифри, у систему порядку від 2 до 36"""
    num_rep={10:'a',
         11:'b',
         12:'c',
         13:'d',
         14:'e',
         15:'f',
         16:'g',
         17:'h',
         18:'i',
         19:'j',
         20:'k',
         21:'l',
         22:'m',
         23:'n',
         24:'o',
         25:'p',
         26:'q',
         27:'r',
         28:'s',
         29:'t',
         30:'u',
         31:'v',
         32:'w',
         33:'x',
         34:'y',
         35:'z'}
    find_non_dig = re.compile(r"\D+")
    non_digs = re.findall(find_non_dig,str(num))
    resulting_num = 0
    to_num = str(num)[::-1]

    for i in range(0,len(to_num)):
        elem = to_num[i]
        try:
            resulting_num += int(elem) * (k**i)
        except:
            for j in range(10,36):
                test = num_rep[j]
                if test == elem:
                    resulting_num += j * (k**i)

    num = resulting_num
    new_num_string=''
    current=num
    while current!=0:
        remainder = current % n
        if 36>remainder>9:
            remainder_string = num_rep[remainder]
        else:
            remainder_string = str(remainder)
        new_num_string = remainder_string + new_num_string
        current = current // n
    return new_num_string

def program():
    # Створення рядку з сімковими числами згідно умови
    set_base7 = ""
    for i in range(0,10):
        num = baseAnytoAny(10, random.randint(1,100), 7)
        set_base7 += num + " "
    set_base7 = set_base7[:-1] + "."

    print(f"Початковий рядок: {set_base7}")

    pattern = re.compile(r"\d+")
    numbers = re.findall(pattern, set_base7)

    # Знаходження найбільшого числа
    mx = 0
    for i in range(0,len(numbers)):
        current = int(numbers[i])
        if current > mx:
            mx = current
    print(f"Найбільше число: {mx}")

    print(f"Найбільше сімкове число в десятковій системі числення: {baseAnytoAny(7,mx,10)} ")

if __name__ == "__main__":
    program()

    