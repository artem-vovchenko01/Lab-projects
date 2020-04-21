import re
type_color = ("red","blue","green","yellow","black","white")

with open("input_color.txt") as f:
    new_color = f.read()

new_color = re.search(r"\w+",new_color)
if new_color == None:
    print("Не знайдено кольору.")
    quit()

if new_color.group().lower() in type_color:
    x = new_color.group().lower()
    print(f"Новий колір: {x}")
else:
    print("Такого типового кольору немає.")

