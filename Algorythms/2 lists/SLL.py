import timeit
import random

class Node:
    """Class which represents a node in a singly-linked list"""

    def __init__(self, value):
        """Node initialization"""
        self.next = None
        self.val = value

class SLL:
    """Class which represents a singly-linked list and incorporates various interfaces to work with it"""

    def __init__(self):
        """List initialization"""
        self.__index_exc = "Invalid index"
        self.__zero_len = "List is of len 0"
        self.__cant_add_exc = "Not all list element could be added. "
        temp = Node(None)
        self.__head = temp
        self.__tail = temp
        self.__size = 0
        self.__iter_temp = None

    def __str__(self):
        """String representation"""
        obj = self.__head.next
        string = "["
        while obj:
            string += obj.val.__str__()
            if obj.next is not None:
                string += ", "
            obj = obj.next
        return string + "]"

    def __len__(self):
        return self.__size

    def __getitem__(self, idx):
        if idx < 0:
            idx += self.__size
        return self.get(idx)

    def __setitem__(self, idx, val):
        if idx < 0: 
            idx += self.__size
        self.sub(idx, val)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__iter_temp == None:
            self.__iter_temp = self.__head
        if self.__iter_temp.next:
            val = self.__iter_temp.next.val
            self.__iter_temp = self.__iter_temp.next
            return val
        else:
            self.__iter_temp = None
            raise StopIteration
        
    def __contains__(self, val):
        return self.find(val) is not None

    def extend(self, iterable):
        """Inserts all elements from iterable in order to the end"""
        for i in iterable:
            self.append(i)

    def append(self, val):
        """Add element to the end"""
        temp = Node(val)
        self.__tail.next = temp
        self.__tail = temp
        self.__size += 1

    def insert(self, val, index=0):
        """Insert element under index in range from 0 to list length both inclusive. Index 0 by default"""
        if index < 0 or index > self.__size:
            raise Exception(self.__index_exc)
        obj = self.__head
        count = 0
        while count != index:
            obj = obj.next
            count += 1
        if self.__size == 0:
            self.append(val)
            self.__size -= 1
        else:
            temp = obj.next
            new = Node(val)
            new.next = temp
            obj.next = new
            if obj == self.__tail:
                self.__tail = new
        self.__size += 1

    def pop(self, index=None):
        """Remove element by given index and get it"""
        if index is None:
            index = self.__size - 1
        if index < 0 or index >= self.__size:
            raise Exception(self.__index_exc)
        count = 0
        obj = self.__head
        while index != count:
            obj = obj.next
            count += 1
        if obj.next is self.__tail:
            obj.next = None
            result = self.__tail
            del self.__tail
            self.__tail = obj
        else:
            temp = obj.next
            obj.next = obj.next.next
            result = temp
            del temp
        self.__size -= 1
        return result.val

    def remove(self, val):
        """Removes first occurrence of value. True if removed, else False"""
        obj = self.__head
        while obj.next:
            if obj.next.val == val:
                temp = obj.next
                obj.next = obj.next.next
                if temp == self.__tail:
                    self.__tail = obj
                self.__size -= 1
                return True
            else:
                obj = obj.next
        return False

    def sub(self, index, val):
        """Substitute the val of the element by given index"""
        if index < 0 or index >= self.__size:
            raise Exception(self.__index_exc)
        count = -1
        obj = self.__head
        while index != count:
            obj = obj.next
            count += 1
        obj.val = val

    def getSum(self):
        """Calculate a sum of elements. Raises an Exception if not
         all elements can be added. Returns None if the list is of 0 length"""
        obj = self.__head.next
        if obj:
            result = obj.val
            obj = obj.next
        else:
            return None
        while obj:
            try:
                result += obj.val
            except:
                raise Exception(self.__cant_add_exc)
            obj = obj.next
        return result

    def find(self, val):
        """Returns the index of the first occurence of given val. None if not found"""
        obj = self.__head
        index = -1
        while obj != self.__tail:
            obj = obj.next
            index += 1
            if obj.val == val:
                return index
        return None

    def findAll(self, val):
        """Returns the list of indexes of all occurrences of given val"""
        obj = self.__head
        index = -1
        indexes = []
        while obj != self.__tail:
            obj = obj.next
            index += 1
            if obj.val == val:
                indexes.append(index)
        return indexes

    def get(self, index):
        """Returns the value contained under given index"""
        if index < 0 or index >= self.__size:
            raise Exception(self.__index_exc)
        obj = self.__head.next
        count = 0
        while count != index:
            obj = obj.next
            count += 1
        return obj.val

    def clear(self):
        """Clears the list"""
        temp = Node(None)
        self.__head = temp
        self.__tail = temp 
        self.__size = 0

    def getReversed(self):
        """Returns reversed SLL"""
        obj = self.__head.next
        lst = SLL()
        while obj != None:
            lst.insert(obj.val)
            obj = obj.next
        return lst

def test_all_methods(size, find, insertions, low_val, high_val, show):
    t_start = timeit.default_timer()
    temp_lst = SLL()
    print("------------------------- testing APPEND -------------------------\n")
    if show:
        print(temp_lst)
    print(f"Appending {size} elements in range from {low_val} to {high_val}: ")
    t1 = timeit.default_timer()
    for i in range(size):
        temp_lst.append(random.randint(low_val, high_val))
    t2 = timeit.default_timer()
    elapsed = round(t2 - t1, 5)
    if show:
        print(temp_lst)
    print(f"Time for append operation, {size} times: " + str(elapsed) + "\n")

    print("------------------------- testing FIND -------------------------\n")
    if show:
        print(temp_lst)
    print(f"Finding {find}, first occurrence: ")
    print(temp_lst.find(find))
    print(f"Finding {find}, all occurrences: ")
    print(temp_lst.findAll(find))
    find_rand = random.randint(low_val, high_val)
    print(f"Finding random value {size} times: ")
    t1 = timeit.default_timer()
    for i in range(size):
        temp_lst.find(find_rand)
    t2 = timeit.default_timer()
    elapsed = round(t2 - t1, 5)
    print(f"Time for find operation, {size} times: " + str(elapsed) + "\n")

    print("------------------------- testing SUM -------------------------\n")
    print("Array sum: ", temp_lst.getSum())
    t1 = timeit.default_timer()
    temp_lst.getSum()
    t2 = timeit.default_timer()
    elapsed = round(t2 - t1, 5)
    print(f"Time for sum operation, 1 time: " + str(elapsed) + "\n")

    print("------------------------- testing INSERT -------------------------\n")
    print("Size before insertions: ", len(temp_lst))
    print(
        f"Inserting {insertions} random numbers in range from {low_val} to {high_val}: "
    )
    for i in range(insertions):
        n = random.randint(low_val, high_val)
        p = random.randint(0, len(temp_lst) - 1)
        if show:
            print(f"Inserting {n} in pos {p}")
        temp_lst.insert(n, p)
        if show:
            print(temp_lst)
    print(f"Inserting random val at random pos {size} times: ")
    t1 = timeit.default_timer()
    for i in range(size):
        n = random.randint(low_val, high_val)
        p = random.randint(0, len(temp_lst) - 1)
        temp_lst.insert(n, p)
    t2 = timeit.default_timer()
    elapsed = round(t2 - t1, 5)
    print("Size after all insertions: ", len(temp_lst))
    print(f"Time for insert operation, {size} times: " + str(elapsed) + "\n")

    print("------------------------- testing GETREVERSED -------------------------\n")
    t1 = timeit.default_timer()
    temp_lst.getReversed()
    t2 = timeit.default_timer()
    if show:
        print(temp_lst)
        print("Reversed list: ")
        print(temp_lst.getReversed())
    elapsed = round(t2 - t1, 5)
    print(f"Time for get_reversed operation, 1 time: " + str(elapsed) + "\n")

    print("------------------------- testing GET -------------------------\n")
    if show:
        print(temp_lst)
    pos = random.randint(0, len(temp_lst) - 1)
    print(f"Getting el at pos {pos}: ")
    print(temp_lst.get(pos))
    print(f"Getting el at random pos {size} times: ")
    t1 = timeit.default_timer()
    for i in range(size):
        pos = random.randint(0, len(temp_lst) - 1)
        temp_lst.get(pos)
    t2 = timeit.default_timer()
    elapsed = round(t2 - t1, 5)
    print(f"Time for get operation, {size} times: " + str(elapsed) + "\n")

    print("------------------------- testing SUB -------------------------\n")
    sub_f = random.randint(low_val, high_val)
    sub_l = random.randint(low_val, high_val)
    sub_m = random.randint(low_val, high_val)
    pos_sub = random.randint(0, len(temp_lst) - 1)
    if show:
        print(temp_lst)
    print(f"Substitute last, val = {sub_l}:")
    temp_lst.sub(len(temp_lst) - 1, sub_l)
    if show:
        print(temp_lst)
    print(f"Substitute at random pos, val = {sub_m}, pos = {pos_sub}")
    temp_lst.sub(pos_sub, sub_m)
    if show:
        print(temp_lst)
    print(
        f"Substitute random el with val in range from {low_val} to {high_val} {size} times: "
    )
    t1 = timeit.default_timer()
    for i in range(size):
        sub_m = random.randint(low_val, high_val)
        temp_lst.sub(random.randint(0, len(temp_lst) - 1), sub_m)
    t2 = timeit.default_timer()
    elapsed = round(t2 - t1, 5)
    print(f"Time for sub operation, {size} times: " + str(elapsed) + "\n")

    print("------------------------- testing POP -------------------------\n")
    print("Tail before: ", temp_lst[-1])
    print("Popping last element: ")
    temp_lst.pop()
    print("Tail after: ", temp_lst[-1])
    if show:
        print(temp_lst)
    pos_r = random.randint(0, len(temp_lst) - 1)
    print(f"Popping el at pos {pos_r}: ")
    temp_lst.pop(pos_r)
    if show:
        print(temp_lst)
    print("Popping el at pos 0: ")
    temp_lst.pop(0)
    if show:
        print(temp_lst)
    print("Popping last el: ")
    temp_lst.pop(len(temp_lst) - 1)
    if show:
        print(temp_lst)
    print(f"Popping el at random index {int(len(temp_lst) / 2)} times: ")
    t1 = timeit.default_timer()
    leng = len(temp_lst)
    for i in range(int(leng / 2)):
        temp_lst.pop(random.randint(0, len(temp_lst) - 1))
    t2 = timeit.default_timer()
    elapsed = round(t2 - t1, 5)
    print(f"Time for pop operation, {size} times: " + str(elapsed) + "\n")

    print("------------------------- testing CLEAR -------------------------\n")
    if show:
        print(temp_lst)
    print("Clearing: ")
    t1 = timeit.default_timer()
    temp_lst.clear()
    t2 = timeit.default_timer()
    print(temp_lst)
    elapsed = round(t2 - t1, 5)
    print(f"Time for clear operation, 1 time: " + str(elapsed) + "\n")
    t_end = timeit.default_timer()
    print(f"All tests ran {t_end - t_start} seconds. ")


if __name__ == "__main__":
    #test_all_methods(3000, 3000, 3000, -10000, 10000, False)
    #test_all_methods(5, 5, 5, -10, 10, True)
    lst = SLL()
    print(lst)
    lst.append(10)
    print(lst)
    lst.extend([3,5,3,10,15,20,4])
    print(lst)
    idx = lst.find(10)  
    print(idx)
    print(lst.get(2))
    print(lst.findAll(10))