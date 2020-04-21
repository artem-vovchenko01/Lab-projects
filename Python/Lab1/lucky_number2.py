lucky = 7

tryout = -1
# Запрошувати введення, допоки не буде введене щасливе число
while tryout != lucky:
    tryout = input("Введіть щасливе число: ")
    # Перейти до наступної ітерації, якщо користувач увів не int
    try:
        tryout = int(tryout)
    except:
        continue

print("Ви вгадали!")
