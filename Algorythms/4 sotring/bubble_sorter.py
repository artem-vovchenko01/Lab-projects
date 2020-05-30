import random

class BubbleSorter:
    def __init__(self, arr):
        self.arr = arr
        
    def sort(self):
        arr = self.arr
        not_sorted = True
        for j in range (len(arr) - 1):
            if not_sorted:
                not_sorted = False
                for i in range( len(arr) - j - 1):
                    if arr[i] > arr[i+1]:
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                        not_sorted = True
            else:
                break
            
def test():
    nums = [random.randint(-100, 100) for i in range(100)]
    sorter = BubbleSorter(nums)
    sorter.sort()
    print(nums)

if __name__ == "__main__":
    test()