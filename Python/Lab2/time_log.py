import time
def log_time():
    '''Повертає простий рядок часу без пробілів, що має формат рядків файлу
    реєстрації. '''
    return ("%4.4d-%2.2d-%2.2dT%2.2d:%2.2d:%2.2d" % time.localtime()[:6])
print(log_time())
