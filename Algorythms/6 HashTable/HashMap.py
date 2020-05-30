from SLL import SLL
import random
import timeit

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
    
    def __str__(self):
        return f"{self.key} : {self.val}"

    def __eq__(self, other):
        """Compares to other node only using key. This convention used for proper storing nodes in HashMap"""
        return self.key == other.key

class HashMap:
    def __init__(self):
        self.__INIT_CAPACITY = 16 # initial capacity 
        self.__MAX_LOAD_FACTOR = 0.7 # maximum load factor. Double capacity
        self.__MIN_LOAD_FACTOR = 0.25 # minimum load factor. Half capacity 
        self.__INCREASE_FACTOR = 2 # how many times capacity increases when reaching MAX_LOAD_FACTOR
        self.__capacity = self.__INIT_CAPACITY # current capacity
        self.__size = 0 # number of non-empty buckets (when linked list in the bucket has >= 1 node)
        self.__pairs = 0 # number of (key : val) pairs. Usually != to size
        self.__arr = [SLL() for i in range(self.__INIT_CAPACITY)] # storage for buckets (SLLs)
        self.__iter_idx = 0 # current arr index. Used for iterator
        self.__iter_idx_sll = 0 # current index of current SLL. Used for iterator

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, val):
        self.put(key, val)

    def __len__(self):
        return self.__pairs

    def __iter__(self):
        return self

    def __next__(self):
        while self.__iter_idx < self.__capacity:
            sll = self.__arr[self.__iter_idx]
            if len(sll) > 0:
                if len(sll) > self.__iter_idx_sll:
                    val = sll[self.__iter_idx_sll]
                    self.__iter_idx_sll += 1
                    return val
                else:
                    self.__iter_idx += 1
                    self.__iter_idx_sll = 0
            else:
                self.__iter_idx += 1
        self.__iter_idx = 0
        self.__iter_idx_sll = 0
        raise StopIteration

    def  __str__(self):
        if self.__size == 0:
            return "{}"
        string = "{"
        for lst in self.__arr:
            for node in lst:
                string += node.__str__() + ", "
        return string + "\b\b}"

    def put(self, key, val):
        """Puts (key, val) pair. Just updates value if this key already present"""
        increasedSize = False
        newNode = Node(key, val)
        h = hash(key) % self.__capacity
        bucket = self.__arr[h]
        if len(bucket) == 0:
            self.__size += 1
            increasedSize = True
        idx = bucket.find(newNode)
        if idx is None:
            bucket.append(newNode)
            self.__pairs += 1
        else:
            bucket.sub(idx, newNode)
        if increasedSize:
            loadFactor = self.__size / self.__capacity
            if loadFactor > self.__MAX_LOAD_FACTOR:
                self.__resize(self.__capacity * self.__INCREASE_FACTOR)

    def get(self, key):
        """Returns value under given key"""
        h = hash(key) % self.__capacity
        sll = self.__arr[h]
        idx = sll.find(Node(key, ""))
        if idx is None:
            return idx
        return sll[idx].val

    def remove(self, key):
        """Removes pair with given key. True if removed, otherwise False"""
        h = hash(key) % self.__capacity
        sll = self.__arr[h]
        if sll.remove(Node(key, "")):
            self.__pairs -= 1
            if len(sll) == 0:
                self.__size -= 1
                loadFactor = self.__size / self.__capacity
                if loadFactor < self.__MIN_LOAD_FACTOR and self.__capacity > self.__INIT_CAPACITY:
                    self.__resize(self.__capacity // 2)
            return True
        return False

    def getKeys(self):
        """Return list of keys"""
        keys = []
        for lst in self.__arr:
            for node in lst:
                keys.append(node.key)
        return keys

    def getValues(self):
        """Returns list of values. Will contain all values present in map thus may contain duplicates"""
        values = []
        for lst in self.__arr:
            for node in lst:
                values.append(node.val)
        return values

    def clear(self):
        """Clear HashMap"""
        self.__init__()

    def getDebugStats(self):
        """Returns tuple in form (capacity, number of buckets, number of pairs)"""
        return (self.__capacity, self.__size, self.__pairs)

    def __resize(self, newCapacity):
        """Helper function for resizing internal array"""
        temp = self.__arr
        self.__arr = [SLL() for i in range(newCapacity)]
        self.__size = 0
        self.__pairs = 0
        self.__capacity = newCapacity
        for lst in temp:
            for node in lst:
                self.put(node.key, node.val)

def test_all_methods(put, minKey, maxKey, remove, get, getValues, getKeys, maxValue, show):
    h = HashMap()
    unique = []
    allKeys = []
    print("Generating input ...")
    for i in range(put):
        key = random.randint(minKey, maxKey)
        if unique.count(key) == 0:
            unique.append(key)
        allKeys.append(key)
    print("Done")
    print(f"Unique keys: {len(unique)}, all: {put}")
    print("------------------------- testing PUT -------------------------\n")
    print(f"Putting pairs, keys in range from {minKey} to {maxKey}. Value range: from 0 to {maxValue}: ")
    allElapsed = 0
    t1 = timeit.default_timer()
    for key in allKeys:
        val = hash(str(timeit.default_timer())) % maxValue
        h.put(key, val)
        if show:
            print(f"Put {key} : {val} pair: ")
            print(h)
    t2 = timeit.default_timer()
    print("Testing put for proper functioning ")
    for pair in h:
        if unique.count(pair.key) == 0:
            print("ERROR NOT PROPERLY FUNCTIONING")
    for key in unique:
        if not h.get(key):
            print("ERROR NOT PROPERLY FUNCTIONING")
    print("Done")

    elapsed = round(t2 - t1, 5)
    allElapsed += elapsed
    print(f"Number of pairs: {len(h)}")
    stat = h.getDebugStats()
    print(f"Current capacity: {stat[0]}, \n Current number of buckets: {stat[1]}")
    print(f"Time for put operation, {put} times: " + str(elapsed) + "\n")

    print("------------------------- testing GET -------------------------\n")
    print("Getting values under random keys")
    t1 = timeit.default_timer()
    if show:
        print(h)
    for i in range(get):
        idx = random.randint(0, len(unique) - 1)
        key = unique[idx]
        val = h.get(key)
        if show:
            print(f"Getting value with key {key} : {val}")
    t2 = timeit.default_timer()
    elapsed = round(t2 - t1, 5)
    allElapsed += elapsed
    print(f"Time for get operation, {get} times: " + str(elapsed) + "\n")

    print("------------------------- testing GETKEYS -------------------------\n")
    print("Testing getKeys(), which returns array of keys")
    t1 = timeit.default_timer()
    for i in range(getKeys):
        arr = h.getKeys()
    if show:
        print(arr)
        print("* showing result only once for avoiding clutter ")
    t2 = timeit.default_timer()

    elapsed = round(t2 - t1, 5)
    allElapsed += elapsed

    print(f"Time for getKeys operation, {getKeys} times: " + str(elapsed) + "\n")

    print("------------------------- testing GETVALUES -------------------------\n")
    print("Testing getValues(), which returns array of values")
    t1 = timeit.default_timer()
    for i in range(getValues):
        arr = h.getValues()
    if show:
        print(arr)
        print("* showing result only once for avoiding clutter ")
    t2 = timeit.default_timer()
    elapsed = round(t2 - t1, 5)
    allElapsed += elapsed

    print(f"Time for getValues operation, {getValues} times: " + str(elapsed) + "\n")

    print("------------------------- testing REMOVE -------------------------\n")
    if remove > len(unique):
        remove = len(unique)
    print(f"Removing {remove} keys: ")
    t1 = timeit.default_timer()
    for i in range(0, remove - 1):
        key = unique[i]
        if show:
            print(f"Removing key {key}: ")
            print(f"Number of pairs: {len(h)}")
        h.remove(key)
        if show:
            print(h)
    t2 = timeit.default_timer()
    elapsed = round(t2 - t1, 5)
    allElapsed += elapsed

    print(f"Number of pairs: {len(h)}")
    print(f"Time for remove operation, {remove} times: " + str(elapsed) + "\n")
    stat = h.getDebugStats()
    print(f"Current capacity: {stat[0]}, \n Current number of buckets: {stat[1]}")
    print(f"Time for all operations: " + str(allElapsed) + "\n")

if __name__ == "__main__":
    #next line for testing for proper functionong with small inputs 
    #test_all_methods(10, 1, 20, 10, 10, 10, 10, 25000, True)
    #next line is for time benchmarking
    #test_all_methods(30_000, -30_000, 30_000, 30_000, 30_000, 100, 100, 1_000_000, False)
    h = HashMap()
    h.put(4, "hello")
    h[100] = "abc"

    print(h)
    print(h[45])
    print(len(h))
