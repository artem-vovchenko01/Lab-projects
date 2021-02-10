import random

class QuickSorter:
    def __init__(self, arr):
        self.arr = arr

    def sort(self):
        self.rec_sort(self.arr, 0, len(self.arr) - 1)

    def rec_sort (self, arr, low, high):
        if low < high:
            pivot = self.partition(arr, low, high)
            self.rec_sort(arr, low, pivot - 1)
            self.rec_sort(arr, pivot + 1, high)

    def partition (self, arr, low, high):
        p_index = low
        pivot = high
        if low < high:
            for i in range(low, high):
                if arr[i] < arr[pivot]:
                    arr[i], arr[p_index] = arr[p_index], arr[i]
                    p_index += 1
        arr[p_index], arr[pivot] = arr[pivot], arr[p_index]
        return p_index

def test():
    nums = [random.randint(-100, 100) for i in range(1000)]
    sorter = QuickSorter(nums)
    sorter.sort()
    print(nums)

if __name__ == "__main__":
    test()