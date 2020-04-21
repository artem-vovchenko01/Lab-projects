import re
string = "Sooomething waas wrronngg wittth tyypeer. Heee waantss too havve a break."

factor = True
# Будемо циклічно заміняти кожна два однакові сусідні елементи
while factor == True:
    for i in range(1,len(string)):
        a = string[i]
        b = string[i-1]
        if a.lower() == b.lower():
            string = re.sub(f"{a}{b}",f"{a}",string)
            break
        if i == len(string) - 1:
            factor = False

print(string)
