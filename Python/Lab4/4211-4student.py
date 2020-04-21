from student import Student
students = {}
persons = []
limit = 500
def command3(): # help
    print("n/N - new student, s/S - show info, h/H - help")

def command2(): # show
    """
    Виведення інофрмації про студента
    """
    global students
    name = input(" Ім'я студента: ")
    for stud in persons:
        if stud.name == name:
            print(stud.printDetails())

def command1(): # new
    """
    Створення студента
    """
    global students
    global limit
    name = input("Ім'я студента: ")
    student = Student(name)

    newcourse = 0
    while newcourse != "stop":     
        newcourse = input ("Уведіть номер курсу або 'stop' ")   
        if newcourse == "stop":
            break
        student.enroll(newcourse)
        
    phone = input("Номер телефона: ")
    email = input("Електронна пошта: ")
    deg = input("Вчений ступінь: ")
    precise = input("Години точних наук на семестр: ")
    hum = input("Години гуманітарних наук на семестр: ")
    if int(precise) + int(hum) > limit:
        print(f"Студент {name} буде перевантажений навчанням! ")
    student.addInfo(phone,email,deg)
    st = student
    info = f"{st.courses}\t{st.phone}\t{st.email}\t{st.deg}"
    students[name] = info 
    persons.append(st)

def chooseComm(com):
    """
    Вибір команди
    """
    if com.lower() == "h":
        command3()
    elif com.lower() == "n":
        command1()
    elif com.lower() == "s":
        command2()
    else:
        print("No such command. ")
        interface()

def interface():
    while True:
        comm = input("Уведіть команду (h - справка) ")
        chooseComm(comm)  

interface()