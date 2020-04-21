import random

class QuickSorter:

    def sort (self, arr, low, high):
        if low < high:
            pivot = self.partition(arr, low, high)
            self.sort(arr, low, pivot - 1)
            self.sort(arr, pivot + 1, high)

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

arr1 = [4,4,6,67,75,65,7,7,6,85,7,6]
arr1 = [random.randint(-1000, 1000) for i in range(0,1000000)]
QuickSorter().sort(arr1, 0, len(arr1) - 1)

print(arr1[-100:-1])