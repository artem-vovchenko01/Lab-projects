from insertion_sort import InsertionSorter
import random
class BucketSorter: 
    def __init__(self, arr):
        self.arr = arr
        
    def bucket_sort(self, n):
        """ Sort using (n + 1) buckets """
        buckets = [[] for i in range(n + 1)]
        result = []
        for el in self.arr:
            buckets[int(el * n)].append(el)
        for bucket in buckets:
            if len(bucket) > 0:
                sorter = InsertionSorter(bucket)
                for el in sorter.sort_asc():
                    result.append(el)
        return result

def test():
    floats = [random.random() for i in range(100)]
    sorter = BucketSorter(floats)
    arr = sorter.bucket_sort(10)
    for el in arr:
        print(el)

if __name__ == "__main__":
    test()