import random
import copy

class InsertionSorter:
    def __init__(self, arr):
        self.__arr = arr

    def sort_asc (self):
        arr = list(self.__arr)
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def sort_desc (self):
        arr = list(self.__arr)
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

    def search (self, item):
        for i in range(0, len(self.__arr)):
            if arr[i] == item:
                return i
        return None

    def get_arr (self):
        return self.__arr

arr = [random.randint(-100, 100) for i in range(100)]

sorter = InsertionSorter(arr)

asc = sorter.sort_asc()
desc = sorter.sort_desc()
search = sorter.search(50)
print(asc)
print(desc)
print(search)