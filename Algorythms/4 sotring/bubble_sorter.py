class BubbleSorter:
    def sort(self, arr):
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
            


arr1 = [4,5,7,8,4,5,7,8,6,44,4,4,4,5,5,5,65]
# arr1 = [3,4,5,6,7,8]
BubbleSorter().sort(arr1)

print(arr1)