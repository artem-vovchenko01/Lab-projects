# Функція, що створює вкладені кортежі з даного списку елементів
def nest(args):
    global ls
    ls = []
    for i in range(0,len(args)):
        ls.append(tuple(args[:len(args)-i]))
    ls = tuple(ls)
    return ls

result = nest(list(range(1,11)))
result1 = nest(["a","b","c","d","e","f"])
print(result)
print(result1)
