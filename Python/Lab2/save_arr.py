# Імпорт необхідних модулів
import pickle
import numpy

sample_arr = numpy.arange(1,101)
# Записуємо дескриптор файлу в змінну. Оскільки файлу з даним ім'ям не існує і 
# використовуэться параметр w, то він буде створений і відкритий для запису
pickle_out = open("stored_arr",'wb')
# Запис масиву в файл
pickle.dump(sample_arr, pickle_out)
# Закриваємо файл, звільнюємо пам'ять
pickle_out.close()
# Відкриваємо файл на зчитування
pickle_in = open("stored_arr", "rb")
# Завантажуємо масив з диска у змінну
restored_arr = pickle.load(pickle_in)

print(restored_arr)

