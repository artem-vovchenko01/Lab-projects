import sqlite3, re

# Власні класи виняткових ситуацій
class wrongDate(Exception):
    pass
class wrongName(Exception):
    pass

# Створюємо базу даних в оперативній пам'яті
conn = sqlite3.connect(":memory:")
cur = conn.cursor()
# Створюємо порожню таблицю
cur.execute("CREATE TABLE employees (Name text, Surname text,BirthDate text)")
conn.commit()

def insert(emp_name,emp_sname,date):
    """
    Функція, що доповнює базу даних рядком з іменем, прізвищем та ЗП працівника
    """
    cur.execute("INSERT INTO employees VALUES (:name,:sname,:date)",{"name":emp_name,"sname":emp_sname,"date":date})
    conn.commit()

def extract():
    """
    Функція, що виводить базу даних у консоль
    """
    cur.execute("SELECT * FROM employees")
    print(cur.fetchall())

def correctPush(name,emp_sname,date):
    """
    Функція, що перевіряє дані на вході і відправляє її ф-ї insert у випадку коректності
    """
    errorlevel = 0
    # re-шаблони
    name_pat = re.compile(r"[A-Z]+")
    date_pat = re.compile(r'[0-3][0-9]\.[0-1][0-9]\.[12]\d{3}')

    name_matches = re.findall(name_pat,name)
    sname_matches = re.findall(name_pat,emp_sname)
    date_matches = re.findall(date_pat,date)
    try:
        if len(name_matches) == 0 or len(sname_matches) == 0:
            raise wrongName("Name or surname passed is incorrect! ")
    except:
        print("Сталася помилка wrongName")
        errorlevel = 1
    try:
        if len(date_matches) == 0:
            raise wrongDate("Date passed is incorrect! ")
    except:
        print("Сталася помилка wrongDate")
        errorlevel = 1
    if errorlevel == 0:
        insert(name,emp_sname,date)

name = "Artem"
emp_sname = "Vovchenko"
date = "24.10.1990"
correctPush(name,emp_sname,date)
extract()
name = "10010101"
emp_sname = "Telenyk"
date = "Zrozumilo?"
correctPush(name,emp_sname,date)
extract()