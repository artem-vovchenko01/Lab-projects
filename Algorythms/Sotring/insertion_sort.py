import random
import copy

class InsertionSorter:
    def __init__(self, arr):
        self.__arr = arr

    def sort_asc(self):
        """ Sort in ascending order """
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
        """ Sort in descending order """
        arr = list(self.__arr)
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr

def test():
    nums = [random.randint(-100, 100) for i in range(100)]
    sorter = InsertionSorter(nums)
    arr = sorter.sort_asc()
    print(arr)
    arr = sorter.sort_desc()
    print(arr)

if __name__ == "__main__":
    test()