class Student:
    '''Зберігає особисті дані студента, email, name ...''' 
    def __init__(self, *args):        
        self.name = args[0]
        self.courses = []
    def printDetails(self): # Виводить атрибути 
        to_return = f"Ім’я:  {self.name}\n" + f"Курси:  {self.courses}\n"
        try:
            to_return += f"Телефон: {self.phone}\n"
        except: pass
        try:
            to_return += f"Пошта: {self.email}\n"
        except: pass
        try:
            to_return += f"Ступінь: {self.deg}\n"
        except: pass
        return to_return
        
    def enroll(self, course): # Додає навчальні курси 
        self.courses.append(course) 
    
    def addInfo(self, phone, email, degree):
        self.phone = phone
        self.email = email
        self.deg = degree
    