class Employee:
    '''Зберігає особисті дані працівника, email, name ...''' 
    def __init__(self, *args):     
        self.name = args[0]   
        self.projects = []
    def __del__(self):
        print(f"{self.name} was fired! ")
    def printDetails(self): # Виводить атрибути 
        to_return = f"Ім’я:  {self.name}\n" + f"Проекти:  {self.projects}\n"
        try:
            to_return += f"Вік: {self.age}\n"
        except: pass
        try:
            to_return += f"Телефон: {self.phone}\n"
        except: pass
        try:
            to_return += f"Пошта: {self.email}\n"
        except: pass
        try:
            to_return += f"Посада: {self.position}\n"
        except: pass
        try:
            to_return += f"Зарплата: {self.pay}\n"
        except: pass

        return to_return
        
    def enroll(self, project): # Додає навчальні курси 
        self.projects.append(project) 
    
    def addInfo(self, phone, email, age, position, pay):
        self.phone = phone
        self.email = email
        self.age = age
        self.position = position
        self.pay = pay

    def promote(self, new_position):
        self.position = new_position

    def changePay(self, percent):
        """
        Змінює зарплату працівника на заданий відсоток
        """
        self.pay = int(self.pay) * ( 100 + int(percent) ) / 100
    
employees = {}
persons = []

def command7(): # exit
    quit()

def command6(): # fire
    name = input("Ім'я працівника: ")
    for emp in persons:
        if emp.name == name:
              persons.remove(emp)
              del emp
              break

def command5(): # promote
    name = input("Ім'я працівника: ")
    for emp in persons:
        if emp.name == name:
            new_position = input("Нова позиція в компанії: ")
            emp.promote(new_position)
            break
            

def command4(): # change pay 
    name = input("Ім'я працівника: ")
    percent = input("Уведіть відсоток зміни (якщо знизити, то з - ) " )
    for emp in persons:
        if emp.name == name:
            emp.changePay(percent)
            break

def command3(): # help
    print("n/N - new employee, s/S - show info, c/C - change pay, h/H - help, p/P - promote, f/F - fire, q/Q - exit")

def command2(): # show
    """
    Виведення інофрмації про студента
    """
    global employees
    name = input(" Ім'я працівника: ")
    for emp in persons:
        if emp.name == name:
            print(emp.printDetails())

def command1(): # new
    """
    Створення студента
    """
    global employees
    global persons
    name = input("Ім'я парцівника: ")
    age = input("Вік: ")
    position = input("Посада: ")
    pay = input("Зарплата: ")
    employee = Employee(name)
    project = 0
    while project != "stop":     
        project = input ("Уведіть назву проекта або 'stop' ")   
        if project == "stop":
            break
        employee.enroll(project)
    phone = input("Номер телефона: ")
    email = input("Електронна пошта: ")
    
    employee.addInfo(phone, email, age, position, pay)
    persons.append(employee)
def chooseComm(com): # вибір команди
    """
    Вибір команди
    """
    if com.lower() == "c":
        command4()
    elif com.lower() == "h":
        command3()
    elif com.lower() == "s":
        command2()
    elif com.lower() == "n":
        command1()
    elif com.lower() == "p":
        command5()
    elif com.lower() == "f":
        command6()
    elif com.lower() == "q":
        command7()
    else:
        print("No such command. ")
        interface()

def interface(): # інтерфейс користувача
    while True:
        comm = input("Уведіть команду (h - справка) ")
        chooseComm(comm) 

interface()