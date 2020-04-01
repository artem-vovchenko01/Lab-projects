# Створюємо клас виняткової ситуації
class wrongArgument(Exception):
    pass

def NameNumPrint(num):   
    if num not in [0,1,2]:
        raise wrongArgument("Неправильний аргумент")
    if num == 0:         
        print ('Нуль') 
    elif num == 1:       
        print ('Один' )  
    elif num == 2:   
        print( 'Два' )

# Обробка виняткової ситуації
try:
    NameNumPrint(3)
except wrongArgument:
    print("Виникла помилка - неправильний аргумент")
try:
    NameNumPrint(2)
except wrongArgument:
    print("Виникла помилка - неправильний аргумент")
