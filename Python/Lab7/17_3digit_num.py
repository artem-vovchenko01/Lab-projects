a = input()
try:
    num3 = int(a[:3])
except:
    print("EXCEPTION!")
    quit()

# Присвоюємо цифри відповідним змінним
c2, c1, c0 = (str(num3))[0], (str(num3)[1]), (str(num3)[2])
print(c2,c1,c0)
