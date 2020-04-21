import numpy, random
count = 200
arr = numpy.random.randint(0,100,count).reshape(20,10)
print(arr)
biggest_in_cols = []
biggest_in_rows = []
# Визначаємо найбільші елементи кожного стовпця та рядка і додаємо їх до відповідних списків
for i in range(0,10):
    biggest_in_cols.append(max(arr[:,i]))
for i in range(0,20):
    biggest_in_rows.append(max(arr[i,:]))
print("Biggest elements in columns: ",biggest_in_cols)
print("Biggest elements in rows: ", biggest_in_rows)
