a, b = 0, 0

a, b = 1, 1
print(a and b)

a, b = 0, 1
print(not a and b)

a, b = 0, 0
print(not (a and b))

a, b = 0, 1
print(a or b)

a, b = 0, 0
print(a or not b)
print(not(a or b))

a,b = 1, 1 
print(not(not a or not b))
print(a and(a or b)) # doesn't depenf on b

a, b, c = 1, 1, 1
print(a and b and c)
print(a and b or c)
print(a and (b or c))
print((a and b) or c)