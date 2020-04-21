# Визначаємо власні класи помилок
class myZeroDivisionError(Exception):
    def __init__(self):
        super().__init__()
        self.error_mesg = "Division by 0 is forbidden. "
    def __str__(self):
        return self.error_mesg

class myOverflowError(Exception):
    def __init__(self):
        super().__init__()
        self.error_mesg = "Number is too large to be handled. "
    def __str__(self):
        return self.error_mesg

class myValueError(Exception):
    def __init__(self): 
        super().__init__()
        self.error_mesg = "Value error. Integer expected. "
    def __str__(self):
        return self.error_mesg

# "Піднімаємо" помилки при деяких небажаних операціях
a = 0
b = 50_000
c = 2.5
try:
    if a != 0:
        print(5 / a)
    else:
        raise(myZeroDivisionError)
except myZeroDivisionError:
    print("myZeroDivisionError has occured")

try:
    if a <= 10_000 and b <= 10_000:
        print(a + b)
    else:
        raise myOverflowError
except myOverflowError:
    print("myOverflowError has occured")

try:
    my_list = [4,5,6,7]
    if type(c) is int and c < len(my_list):
        print(my_list[c])
    else:
        raise myValueError
except myValueError:
    print("myValueError has occured.")
