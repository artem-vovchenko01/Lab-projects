import re
string = "Hello, here's some a's, you know? hahaha, yeah!"
# Виконуємо необхідну заміну за допомогою методу re.sub()
new_str = re.sub("a","a".upper(),string)
print(new_str)
