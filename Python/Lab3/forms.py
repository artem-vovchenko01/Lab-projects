import re
name = input("Your name: ")
surname = input("Your surname")
birth = input("Birth date")
city = input("Home town / city / village: ")
# Використані регулярні вирази
pat1 = re.compile(r"\w+[-]?")
pat2 = re.compile(r"\d")
name_iter = re.findall(pat1,name)
surname_iter = re.findall(pat1,surname)
city_iter = re.findall(pat1,city)
date_iter = re.findall(pat2, birth)
date_iter = "".join(map(str,date_iter))
print(date_iter)
name = str(); surname = str(); initials = str(); city = str(); birth = str()

# Формування результатів за допомогою циклу
for match in name_iter:
    init = match[0].upper()
    name += f"{init}{match[1:]} "
    if name[-1] == " ": name = name[:-1]
    initials += f"{init}. "

for match in surname_iter:
    init = match[0].upper()
    surname += f"{init}{match[1:]} "
    initials += f"{init}. "
    if surname[-1] == " ": surname = surname[:-1]

for match in city_iter:
    init = match[0].upper()
    city += f"{init}{match[1:]} "
    if city[-1] == " ": city = city[:-1]
birth = f"{date_iter[:2]}.{date_iter[2:4]}.{date_iter[4:]}"

def formatting(name,surname,initials,city,birth):
    """ Функція форматованого виведення"""
    a="NAME"; b="SURNAME"; c="INITIALS"; d="CITY / VILLAGE"; e="BIRTHDATE"
    print(f"{a.ljust(20)}{b.ljust(20)}{c.ljust(20)}{d.ljust(20)}{e.ljust(20)}")
    print(f"{name.ljust(20)}{surname.ljust(20)}{initials.ljust(20)}{city.ljust(20)}{birth.ljust(20)}")
formatting(name,surname,initials,city,birth)
