import re

with open("sample_text.txt") as f:
    text = f.read()
# Видаляємо зайві пропуски за допомогою re.sub()
text = re.sub(r"\s{2,}"," ",text)

print(text)
