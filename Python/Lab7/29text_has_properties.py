def base_convert(k,num,n):
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
    
import re
# Читаємо відповідний файл
with open("29text.txt") as f:
    text = f.read()

pattern = re.compile(r"\w+")
match = re.search(pattern,text)
factor = ""
try:
    int(match.group())
except:
    # Якщо не можна визначити цифрове число, то з ним потрібно працювати, як з цифро-буквеним
    factor = "not_eval"


if factor != "not_eval":
    # Рахуємо суму цифр
    summ = sum(map(lambda x: int(x),match.group()))
    # Конвертуємо число з сімкової системи в десяткову
    num7 = int(base_convert( 7, str(match.group()), 10 ))
    # Обробка ситуацій відповідно до ТЗ
    if summ % 9 == 0:
        print("Десяткове число в текстовому файлі ділиться на 9")
    else:
        print("Десяткове число в текстовому файлі не ділиться на 9")
    if int(match.group()) % 4 == 0:
        print("Десяткове число в текстовому файлі ділиться на 4")
    else:
        print("Десяткове число в текстовому файлі не ділиться на 4")
    if summ % 2 == 0 and summ % 3 == 0:
        print("Десяткове число в текстовому файлі ділиться на 6")
    else:
        print("Десяткове число в текстовому файлі не ділиться на 6")
    if num7 % 2 == 0:
        print("Число в текстовому файлі парне в сімковій системі")
    else:
        print("Число в текстовому файлі не є парним в сімковій системі")
    if text[0] == "0" and "0123456789".startswith(text):
        print("Текст є початковим фрагментом з 0123456789")
    else:
        print("Текст не є початковим фрагментом з 0123456789")      
    if text[-1] == "9" and "0123456789".endswith(text):
        print("Текст є кінцевим фрагментом з 0123456789")
    else:
        print("Текст не є кінцевим фрагментом з 0123456789")  
    pattern2 = re.compile(r"[0-9]+")
    pattern3 = re.compile(r"\d+")
    match2 = re.match(pattern2,text)
    match3 = re.match(pattern3,text)

    if match2 != None:
        count_suitable = 0
        for i in range(1,len(text)):
            if int(text[i]) - int(text[i-1]) == 1:
                count_suitable += 1
        if count_suitable == len(text) - 1:
            print("Текст є частиною 0123456789")
        else:
            print("Текст не є частиною 0123456789")
    else:
        print("Текст не є частиною 0123456789")

    if match3 != None:
        to_test = match3.group()
        for i in range(0,len(to_test)):
            if len(to_test) == 1:
                coef = to_test[0]
                print(f"Текст утворює арифметичну прогресію, d = {coef}")
                print("a")
                break
            else:
                coef = int(to_test[1]) - int(to_test[0])
                if i>0:
                    if int(to_test[i]) - int(to_test[i-1]) != coef:
                        print("Текст не становить арифметочної прогремії")
                        break
            if i == len(to_test) -1:
                print(f"Текст утворює арифметичну прогресію, d = {coef} ")
                    
else: print("Не десяткове число")

factor2 = ""
# Пробуємо конвертувати даний рядок у шістнадцяткове число
try:
    num16 = int(base_convert( 16, str(match.group()), 10 ))
except: 
    factor2 = "not_eval"
not_eval = re.compile(r"\W")
find_not_eval = re.search(not_eval,text)
if find_not_eval != None:
    factor2 = "not_eval"
# Обробка шаблонів відповідно до ТЗ
if factor2 != "not_eval":
    if num16 % 5 == 0:
        print("Число в текстовому файлі ділиться на 5 у шістнадцятковій системі")
    else:
        print("Число в текстовому файлі не ділиться на 5 у шістнадцятковій системі")
    num_count = 0
    
    for i in range(0,len(text)):
        if text[i] in "0123456789":
            num_count += 1
        if i == len(text) - 1:
            try:
                int(text[0])
            except:
                print("Умова 'Текст починається з цифри, а далі - букви в кількості, рівній даній цифрі' не виконується")
                break
            if text[0] in "123456789" and num_count == 1 and int(text[0]) == len(text) - 1:
                print("Текст починається з цифри, а далі - букви в кількості, рівній даній цифрі")
            else: 
                print("Умова 'Текст починається з цифри, а далі - букви в кількості, рівній даній цифрі' не виконується")

    num_count = 0
    for i in range(0,len(text)):
        if text[i] in "0123456789":
            num_count += 1
        if i == len(text) - 1:
            try:
                int(text[-1])
            except:
                print("Умова 'Текст закінчується цифрою, а перед нею - букви в кількості, рівній даній цифрі' не виконується")
                break
            if text[-1] in "123456789" and num_count == 1 and int(text[-1]) == len(text) - 1:
                print("Текст закінчується цифрою, а перед нею - букви в кількості, рівній даній цифрі")
            else: 
                print("Умова 'Текст закінчується цифрою, а перед нею - букви в кількості, рівній даній цифрі' не виконується")

    pattern4 = re.compile(r"\d")
    one_dig = re.findall(pattern4,text)
    if len(one_dig) == 1 and int(one_dig[0]) == len(text):
        print("У тексті є лише одна цифра, і вона = довжині тексту")
    else:
        print("Умова 'У тексті є лише одна цифра, і вона = довжині тексту' не виконується")
    if sum(map(lambda x: int(x),one_dig)) == len(text):
        print("Сума цифр у тексті = його довжині")
    else:
        print("Умова 'Сума цифр у тексті = його довжині' не виконується")

else: print("Не число")
