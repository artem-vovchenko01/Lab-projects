import re
string = "Here we are. Yet another competition - A vs O. Who will win? What do you think? Leave your comment below in the comment section!"

# Визначаємо необхідні шаблони регулярних виразів
pat1 = re.compile(r"[aA]")
pat2 = re.compile(r"[oO]")
a_letters = re.findall(pat1,string)
o_letters = re.findall(pat2,string)

# Рахуємо к-сть літер
if len(a_letters) > len(o_letters):
    print("Літер Ф більше")
elif len(o_letters) > len(a_letters):
    print("Літер О більше")
else:
    print("А і О однакова кількість")
    