#Функції-вміння
def m_fly(self):
    print("Я літаю.")
def m_swim(self):
    print("Я пливу.")
def m_sing(self):
    print("Я співаю.")

class Everybody:
    # Базовий клас із методами
    def i_am(self):
        return "Я %s." % self.name
    def __getattr__(self, attname):
        ''' Спеціальний метод класу. Викликається, якщо немає атрибута класу з
        таким іменем '''
        def cant():
            print(self.cant_do(attname))
        return cant
    def cant_do (self, action):
        return str("Я не вмію %s." % action)

    def __str__(self):
        return "Я %s." % self.name

class Fish(Everybody):
    name = "Риба"
    swim = m_swim

class Mermaid(Everybody):
    name = "Русалка"
    sing = m_sing
    swim = m_swim

class Bird(Everybody):
    name = "Птах"
    fly = m_fly
    sing = m_sing

class Man(Everybody):
    name = "Людина"
    sing = m_sing

f = Fish(); r = Mermaid(); b = Bird(); m = Man()
print (f.i_am())
print()
f.swim() 
f.sing()
f.fly()
print()

print (r.i_am())
print()
r.swim()
r.sing()
r.fly()
print()

print (b.i_am())
print()
b.swim()
b.sing()
b.fly()
print()

print (m.i_am())
print()
m.swim()
m.sing()
m.fly()
print()

print ("Людей навчили плавати.")
print()
Man.swim = m_swim
m.i_am()
m.swim()
m.sing()
m.fly()

print()
print(f, r, b, m)