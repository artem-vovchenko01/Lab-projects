import re

with open("sample_text.txt") as f:
    text = f.read()

counter = 0
d_counter = 0
e3_counter = 0 
# Regex шаблони
pattern = re.compile(r" [aA]\w*")
pattern2 = re.compile(r"\w*w")
pattern3 = re.compile(r"\w+")

word_list = re.findall(pattern3, text)
print(word_list)

# Кожне слово перевіряємо циклом за заданими критеріями
for i in range(0,len(word_list)):
    if word_list[i][0].lower() == word_list[i][-1].lower():
        counter += 1
    if "d" in word_list[i] or "D" in word_list[i]:
        d_counter += 1
    e_counter = 0
    for k in range(0,len(word_list[i])):
        if word_list[i][k].lower() == "e":
            e_counter += 1
    if e_counter == 3:
        e3_counter += 1


words = re.findall(pattern,text)
words1 = re.findall(pattern2,text)
print(f"Кількість слів, що починаються на 'a': {len(words)}")
print(f"Кількість слів, що закінчуються на 'w': {len(words1)}")
print(f"Кількість слів, що починаються і закінчуються на одну і ту ж букву: {counter}")
print(f"Кількість слів, що містять хоча б 1 літеру d: {d_counter}")
print(f"Кількість слів, що містять 3 букви е: {e3_counter}")
