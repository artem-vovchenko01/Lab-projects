with open("sample_text.txt") as f:
    text = f.read()
index = None
# Знаходимо індекс першого входження а
for i in range(0,len(text)):
    char = text[i]
    if char.lower() == "a" and i != len(text)-1:
        index = i
        break
result = None
# Якщо символ - латинський, то він і є відповіддю
for i in range(index + 1, len(text)):
    char = text[i]
    if 97 <= ord(char.lower()) <= 122:
        result = char
        break
if index == None or result == None:
    print("False")
print(result)
