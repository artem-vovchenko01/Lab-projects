import sqlite3
import pickle
def _test():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE employees (Name text, Surname text,Payout integer)")
    conn.commit()

    def insert(emp_name,emp_sname,pay):
        cur.execute("INSERT INTO employees VALUES (:name,:sname,:pay)",{"name":emp_name,"sname":emp_sname,"pay":pay})
        conn.commit()

    def extract(val):
        if len(val) == 0:
            cur.execute("SELECT * FROM employees")
            print(cur.fetchall())
            to_pickle = list(cur.execute("SELECT * FROM employees"))
            return to_pickle
        else:
            cur.execute("SELECT * FROM employees WHERE Name=:name",{"name":val})
            print(cur.fetchall())

    def lsall():
        cur.execute("SELECT Name FROM employees")
        print(cur.fetchall())

    def delete(nm,snm):
        cur.execute("DELETE FROM employees WHERE Name = :name AND Surname =:sname",{"name":emp_name,"sname":emp_sname})
        conn.commit()

    def pick():
        w = open("db_pickle",'wb')
        pickle.dump(extract(""), w)
        print("Pickling done!")
        w.close()
        try:
            w = open("db_pickle","rb")
            x = pickle.load(w)
            print(x)
            print("Unpickling done!")
        except FileNotFoundError:
            print("Woops, no such file! ")
            quit()

    def check(chck):
        cur.execute("SELECT * FROM employees WHERE Surname=:sname",{"sname":chck})
        if len(cur.fetchall()) > 0:
            print("Наявний у базі")
        else: 
            q = input("Такий запис відсутній у базі. Додати? y / n ")
            if q == "y":
                emp_name = input("Ім'я працівника: ")
                try:
                    pay = int(input("ЗП працівника: "))
                except:
                    print("Incorrect value. Try again")
                    quit()
                insert(emp_name,chck,pay)

    def format(lst):
        tup = list(cur.execute("SELECT * FROM employees"))
        if len(lst) > 0:
            tup = lst
        f = open("formatted.txt","w")
        f.close()
        f = open("formatted.txt","a")
        a = "Ім'я"
        b = "Прізвище"
        c = "Зарплата"
        top = a.ljust(20)+b.ljust(20)+c.rjust(20)
        f.write(top+"\n")
        line1,line2,line3 = "","",""
        for i in range(0,len(tup)):
            line1 = f"{tup[i][0]}".ljust(24)
            line2 = f"{tup[i][1]}".ljust(28)
            line3 = f"{tup[i][2]}".rjust(0)
            f.write(line1+line2+line3+"\n")
        f.close()
        f = open("formatted.txt")
        print(f.read())
        f.close()

    def salary(name, sname, percent):
        try:
            quotient = (100 + percent) / 100
        except ZeroDivisionError:
            print("Division by 0 is forbidden!")
            quit()
        cur.execute("UPDATE employees SET Payout=Payout*:q WHERE Name=:name AND Surname=:sname",{"q":quotient,"name":name,"sname":sname})
        conn.commit()

    def sort(choice):
            cur.execute("SELECT * FROM employees")
            to_sort = list(cur.execute("SELECT * FROM employees"))
            if choice == "1":
                to_sort.sort(key=lambda x: x[0])
            elif choice == "2":
                to_sort.sort(key=lambda x: x[1])
            else: to_sort.sort(key=lambda x: x[2])
            format(to_sort)

    factor = ""
    while factor != "n" and factor != "N":
        action = input("Action: a - add, d = delete, f - find, l - list all names, p - test pickle, c - check worker by surname, u - update worker's salary, s - sort: ")
        if action == "a":
            emp_name = input("Name: ")
            emp_sname = input("Surname: ")
            sn = emp_name[0].upper()
            ss = emp_sname[0].upper()
            emp_name = f"{sn}{emp_name[1:]}"
            emp_sname = f"{ss}{emp_sname[1:]}"
            try:
                pay = int(input("Salary: "))
            except:
                print("Incorrect value. Try again")
                break
            insert(emp_name,emp_sname,pay)
        elif action == "d":
            emp_name = input("Name: ")
            emp_sname = input("Surname: ") 
            delete(emp_name,emp_sname)
        elif action == "f":
            val = input("Name (leave empty to show all): ")
            extract(val)
        elif action == "l":
            lsall()
        elif action == "p":
            pick()
        elif action == "c":
            chck = input("Surname: ")
            check(chck)
        elif action == "fm":
            format([])
        elif action == "s":
            choice = input("Sort by: 1 - name, 2- surname, 3 - salary: ")
            if choice!="1" and choice!="2" and choice!= "3":
                print("Incorrect value. Try again. ")
                quit()
            sort(choice)
        elif action == "u":
            emp_name = input("Name: ")
            emp_sname = input("Surname: ") 
            q = input("Increase or decrease salary? + / -: ")
            sign = None
            percent = None
            if q == "+":
                sign = 1
            elif q == "-":
                sign = -1
            else: 
                print("Incorrect value. Try again. ")
                quit()
            try:
                percent = sign * int(input("Change by, %: "))
            except:
                print("Incorrect value. Try again. ")
                quit()
            salary(emp_name,emp_sname,percent)
        else: 
            print("No such option. Try again. ")
            break
        factor = input("Continue? y / n: ")
        if factor != "n" and factor != "N" and factor != "y" and factor != "Y":
            print("Incorrect value. Try again.")
            break

if __name__ == "__main__":
    _test()