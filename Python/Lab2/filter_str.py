a = ['a', '4', 'b', 'c', 'F'] 
# Що має вийти
sample = list(filter(lambda x: '3'<x<'b', a) )
result = []
# Цикл, що робить те саме, що і map у даному випадку
for i in range(0,len(a)):
    if "3" < a[i] < "b":
        result.append(a[i])

print(sample)
print(result)
