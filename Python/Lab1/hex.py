num = input()

try:
    num = int(num)
except:
    print("Помилка введення")
    quit()

if num in range(0, 16):
    hex_res = hex(num)
    res = str(hex_res)
    print(res[2])
else:
    print("Помилка введення")