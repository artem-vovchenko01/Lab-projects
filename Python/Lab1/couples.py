string = input()
# Використаємо зріз перших 80 символів
string = string[:81]

# Перевірка 2-х сусідніх елементів на рівність
for i in range(0, len(string)-1):
    if string[i] == string[i+1]:
        print(string[i]+string[i+1])