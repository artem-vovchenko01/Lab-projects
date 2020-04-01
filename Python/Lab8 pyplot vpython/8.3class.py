from matplotlib import pyplot as plt

sex = [8, 22]
f1 = plt.figure()
plt.pie(sex, labels = ["Дівчата","Хлопці"], colors = ["pink","b"],startangle=90)
plt.title("Кількість хлопців та дівчат")
f1.show()

years = [2000, 2001, 2002]
freq = [12,14,4] # I didn't find correct data, so it's just a sample
f2 = plt.figure()
plt.bar(years, freq)
plt.title("Розподіл за роками народження")
f2.show()

town = [5, 25]
f3 = plt.figure()
plt.pie(town, labels = ["Кияни","Іногородні"], colors = ["g","b"],startangle=90)
plt.title("Розподіл за місцем проживання")
f1.show()

plt.show()