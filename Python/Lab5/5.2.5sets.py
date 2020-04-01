class Set:
    def __init__(self, *vals):
        """
        Створення множини із заданими даними або без них
        """
        _first_iter = 0
        self.s = {}
        self.tp = None
        for key in vals:
            if _first_iter == 0:
                self.tp = type(key)
            if type(key) != self.tp:
                print("Type should be the same for all passed values. ")
                self.s = {}
                return
            _first_iter = 1
            self.s[key] = None
    
    def __len__(self):
        """
        Спеціальний метод для виведення довжини об'єкту функцією len
        """
        return len(self.s)

    def __str__(self):
        """
        Спеціальний метод для виведення об'єкту в рядковому форматі.
        """
        result = []
        for key in self.s.keys():
            result.append(key)
        return str(result)

    def union(self, other):
        """
        Об'єднання двох множин
        """
        ls = other.s.keys()
        for key in ls:
            self.s[key] = None

    def intersection(self, other):
        """
        Перетин двох множин
        """
        new_s = {}
        ls1 = self.s.keys()
        ls2 = other.s.keys()
        for key in ls1:
            if key in ls2:
                new_s[key] = None
        return list(new_s.keys())

    def difference(self, other):
        """
        Різниця двох множин
        """
        new_s = {}
        ls1 = self.s.keys()
        ls2 = other.s.keys()
        for key in ls1:
            new_s[key] = None
            if key in ls2:
                del new_s[key]
        return list(new_s.keys())

    def isEmpty(self):
        """
        Перевірка множини на порожність
        """
        return len(self.s) == 0

    def add(self, *vals):
        """
        Додавання елементів до множини
        """
        for key in vals:
            self.s[key] = None

    def remove(self, *vals):
        """
        Видалення елементів з множини
        """
        for key in vals:
            if key not in self.s.keys():
                print("Key Error! ")
                return
            del self.s[key]

    def mx(self):
        """
        Максимальний елемент
        """
        ls = list(self.s.keys())
        return max(ls)
    
    def mn(self):
        """
        Мінімальний елементе
        """
        ls = list(self.s.keys())
        return min(ls)

    def copy(self):
        """
        Повернення копії об'єкту
        """
        ls = list(self.s.keys())
        obj = Set(*ls)
        return obj


print("Створимо декілька множин. ")
s1 = Set(4,5,6)
s2 = Set(10, 4, 3)
print(f"s1: {s1}")
print(f"s2: {s2}\n")
new = [8, 7, 9, 7]
print(f"Додамо елементи зі списку: {new} у множину s1")
s1.add(*new)
print(s1, "\n")
print("Потужність множини s1: ")
print(len(s1), "\n")
print(f'Визначимо перетин множин {s1} та {s2} :')
inter = s1.intersection(s2)
print(inter, "\n")
print(f"Визначимо об'днання даних множин. ")
s3 = s1.copy()
s1.union(s2)
print(s1, "\n")
print(f"Визначимо різницю множин {s1} і {s3}")
print(s1.difference(s3), "\n")
print(f"Максимальний та мінімальний елемент множини {s1}: ")
print(f"MAX: {s1.mx()}, MIN: {s1.mn()}")
