Header = ('FIO','BIRTH DATE','AGE')
def MyBaseInit():
    ''' Процедура ініціалізації бази. Створюється порожній словник з
    кортежем, що містить імена полів '''
    A = dict()
    base = (Header,A)
    return base

def MyBaseAppendRecord(A,FIO,BIRTH_DATE,AGE):
    '''Додавання запису в базу '''
    A[1][FIO]=[BIRTH_DATE,AGE]

def MyBaseDeleteRecord(A,FIO):
    '''Видалення запису з бази '''
    del[A[1][FIO]]
