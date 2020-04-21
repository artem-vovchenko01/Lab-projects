# Визначаємо, скільки кілометрів у милі і навпаки
mile = 1.609344
km = 1/mile

# Конвертуємо милі в кілометри
for i in range(100, 1001, 100):
    mile_convert = round(i * mile, 3)
    mile_convert = str(mile_convert)
    i = str(i)
    print("У " + i + " миль - " + mile_convert + " кілометрів.")
   
# Конвертуємо кілометри в милі
for i in range(100, 1001, 100):
    km_convert = round(i * km, 3)
    km_convert = str(km_convert)
    i = str(i)
    print("У " + i + " кілометрів - " + km_convert + " миль.")
