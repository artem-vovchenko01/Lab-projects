st = "ABCDEFGHIJ"
nums = "0123456789"
print(st)
# Цикли, що виводить рядки за вказаним у завданні шаблоном
for i in range(len(st),0,-1):
    res = ""
    res = f'{st[:i-1]}{nums[i-1:]}'
    print(res)
for i in range(0,len(st)):
    res = ""
    res = f'{st[:i+1]}{nums[i+1:]}'
    print(res)