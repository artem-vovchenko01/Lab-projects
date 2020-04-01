class Rev:
    def __init__(self, value):
        """
        Метод виконує реверс в залежності від типу об'єкта
        """
        self.res = None
        self.value = value
        if type(value) is str:
            self.res = ""
            ls = list(value)
            ls.reverse()
            for let in ls:
                self.res += let

        if type(value) is list:
            ls = list(value)
            ls.reverse()
            self.res = str(ls)

        if type(value) is tuple:
            self.res = ()
            for i in range(len(value) -1, -1, -1):
                self.res += (value[i],)
            self.res = str(self.res)
            
    def __str__(self):
        """
        Спеціальний метод для рядкового виведення
        """
        return self.res

str1 = "Hello"
rv = Rev(str1)
print(str1)
print(f"Reversed: {rv}", "\n")

list1 = [4, 3, 5, 9]
rv2 = Rev(list1)
print(list1)
print(f'Reversed: {rv2}', "\n")

tuple1 = (4,1,2,0,8)
rv3 = Rev(tuple1)
print(tuple1)
print(f"Reversed: {rv3}")