with open("sample_text.txt") as f:
    text = f.read()

num_a = 0
num_b = 0 
# Рахуємо к-сть а та b
for char in text:
    if char.lower() == "a":
        num_a +=1
    if char.lower() == "b":
        num_b +=1
if num_a > num_b:
    print("Літер А більше")
elif num_b > num_a:
    print("Літер B більше")
else: print("Однакова кількість літер А та В")
