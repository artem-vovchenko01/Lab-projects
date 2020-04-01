with open("input.txt") as f:
    text = f.read()

print(f"Початковий рядок: {text}")
# Щоб вилучити крапку, що є останнім символом, з рядка, скористаємося зрізом
s = text[:-1] + " "*20 + "* there was spaces."
print(f"Кінцевий рядок: {s}")
