a = ['a', '4', 'b', 'c', 'F'] 
# Що має вийти
sample = list(map(lambda x: x+'-symbol', a) )
result = []
# Цикл, що робить те саме, що і map у даному випадку
for i in range(0,len(a)):
    result.append((a[i]+"-symbol"))

print(sample)
print(result)