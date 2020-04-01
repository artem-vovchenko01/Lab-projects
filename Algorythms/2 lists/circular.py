import timeit
import random


class Node:
    """Class which represents a node in a circular-linked list, singly-linked implementation"""

    def __init__(self, value):
        """Node initialization"""
        self.next = None
        self.val = value


class CircularLinkedList:
    """Class which represents a circular-linked list and incorporates various interfaces to work with it"""

    def __init__(self):
        """List initialization"""
        self.__index_exc = "Index should be in range from 0 to (list length - 1)"
        self.__zero_len = "List is of len 0"
        self.__not_all_nums = "Not all list elements are numbers. "
        temp = Node(None)
        temp.next = temp
        self.__head = temp
        self.__tail = temp
        self.__size = 0

    def __str__(self):
        """String representation"""
        obj = self.__head.next
        string = "["
        while not obj == self.__head:
            string += obj.val.__str__()
            if not obj.next == self.__head:
                string += ", "
            obj = obj.next
        return string + "]"

    def __len__(self):
        return self.__size

    def add(self, val):
        """Add element to the end"""
        temp = Node(val)
        self.__tail.next = temp
        self.__tail = temp
        temp.next = self.__head
        self.__size += 1

    def insert(self, index, val):
        """Insert element under index in range from 0 to list length"""
        if index < 0 or index > self.__size:
            raise Exception(self.__index_exc)
        obj = self.__head
        count = 0
        while count != index:
            obj = obj.next
            count += 1
        if self.__size == 0:
            self.add(val)
        else:
            temp = obj.next
            new = Node(val)
            new.next = temp
            obj.next = new
            if obj == self.__tail:
                self.__tail = new
        self.__size += 1

    def rem_last(self):
        """Remove last element"""
        if self.__size > 0:
            obj = self.__head
            while obj.next != self.__tail:
                obj = obj.next
            obj.next = self.__head
            del self.__tail
            self.__tail = obj
        else:
            raise Exception(self.__zero_len)
        self.__size -= 1

    def remove(self, index):
        """Remove element by given index"""
        if index < 0 or index >= self.__size:
            raise Exception(self.__index_exc)
        count = 0
        obj = self.__head
        while index != count:
            obj = obj.next
            count += 1
        if obj.next is self.__tail:
            obj.next = self.__head
            del self.__tail
            self.__tail = obj
        else:
            temp = obj.next
            obj.next = obj.next.next
            del temp
        self.__size -= 1

    def sub_last(self, val):
        """Substitute the val of the last element"""
        if self.__size > 0:
            self.__tail.val = val
        else:
            raise Exception(self.__zero_len)

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

    def get_sum(self):
        """Calculate a sum of elements. Raises an Exception if not
         all elements are numbers. Returns None if the list is of 0 length"""
        result = 0
        obj = self.__head.next
        while not obj == self.__head:
            try:
                result += float(obj.val)
            except:
                raise Exception("Not all list elements are numbers. ")
            obj = obj.next
        if self.__size == 0:
            raise Exception(self.__zero_len)
        else:
            return result

    def find(self, val):
        """Returns the index of the first occurence of given val"""
        obj = self.__head
        index = -1
        while obj != self.__tail:
            obj = obj.next
            index += 1
            if obj.val == val:
                return index
        return None

    def find_all(self, val):
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

    def get_last(self):
        """Returns tail's value"""
        if self.__size > 0:
            return self.__tail.val
        else:
            raise Exception(self.__zero_len)

    def clear(self):
        """Clears the list"""
        while self.__size > 0:
            self.rem_last()

    def get_reversed(self):
        """Returns reversed DoublyLinkedList"""
        obj = self.__head.next
        lst = CircularLinkedList()
        while obj != self.__head:
            lst.insert(0, obj.val)
            obj = obj.next
        return lst


def test_all_methods(size, find, insertions, low_val, high_val, show):
    t_start = timeit.default_timer()
    temp_lst = CircularLinkedList()
    print("------------------------- testing ADD -------------------------\n")
    if show:
        print(temp_lst)
    print(f"Adding {size} elements in range from {low_val} to {high_val}: ")
    t1 = timeit.default_timer()
    for i in range(size):
        temp_lst.add(random.randint(low_val, high_val))
    t2 = timeit.default_timer()
    elapsed = t2 - t1
    if show:
        print(temp_lst)
    print(f"Time for add operation, {size} times: " + str(elapsed) + "\n")

    print("------------------------- testing FIND -------------------------\n")
    if show:
        print(temp_lst)
    print(f"Finding {find}, first occurrence: ")
    print(temp_lst.find(find))
    print(f"Finding {find}, all occurrences: ")
    print(temp_lst.find_all(find))
    find_rand = random.randint(low_val, high_val)
    print(f"Finding random value {size} times: ")
    t1 = timeit.default_timer()
    for i in range(size):
        temp_lst.find(find_rand)
    t2 = timeit.default_timer()
    elapsed = t2 - t1
    print(f"Time for find operation, {size} times: " + str(elapsed) + "\n")

    print("------------------------- testing SUM -------------------------\n")
    print("Array sum: ", temp_lst.get_sum())
    t1 = timeit.default_timer()
    temp_lst.get_sum()
    t2 = timeit.default_timer()
    elapsed = t2 - t1
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
        temp_lst.insert(p, n)
        if show:
            print(temp_lst)
    print(f"Inserting random val at random pos {size} times: ")
    t1 = timeit.default_timer()
    for i in range(size):
        n = random.randint(low_val, high_val)
        p = random.randint(0, len(temp_lst) - 1)
        temp_lst.insert(p, n)
    t2 = timeit.default_timer()
    elapsed = t2 - t1
    print("Size after all insertions: ", len(temp_lst))
    print(f"Time for insert operation, {size} times: " + str(elapsed) + "\n")

    print("------------------------- testing GET_REVERSED -------------------------\n")
    t1 = timeit.default_timer()
    temp_lst.get_reversed()
    t2 = timeit.default_timer()
    if show:
        print(temp_lst)
        print("Reversed list: ")
        print(temp_lst.get_reversed())
    elapsed = t2 - t1
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
    elapsed = t2 - t1
    print(f"Time for get operation, {size} times: " + str(elapsed) + "\n")

    print("------------------------- testing SUB -------------------------\n")
    sub_f = random.randint(low_val, high_val)
    sub_l = random.randint(low_val, high_val)
    sub_m = random.randint(low_val, high_val)
    pos_sub = random.randint(0, len(temp_lst) - 1)
    if show:
        print(temp_lst)
    print(f"Substitute last, val = {sub_l}:")
    temp_lst.sub_last(sub_l)
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
    elapsed = t2 - t1
    print(f"Time for sub operation, {size} times: " + str(elapsed) + "\n")

    print("------------------------- testing REMOVE -------------------------\n")
    print("Tail before: ", temp_lst.get_last())
    print("Removing last element, using rem_last(): ")
    temp_lst.rem_last()
    print("Tail after: ", temp_lst.get_last())
    if show:
        print(temp_lst)
    pos_r = random.randint(0, len(temp_lst) - 1)
    print(f"Removing el at pos {pos_r}: ")
    temp_lst.remove(pos_r)
    if show:
        print(temp_lst)
    print("Removing el at pos 0: ")
    temp_lst.remove(0)
    if show:
        print(temp_lst)
    print("Removing last el using remove(len(lst)-1): ")
    temp_lst.remove(len(temp_lst) - 1)
    if show:
        print(temp_lst)
    print(f"Removing el at random index {int(len(temp_lst) / 2)} times: ")
    t1 = timeit.default_timer()
    leng = len(temp_lst)
    for i in range(int(leng / 2)):
        temp_lst.remove(random.randint(0, random.randint(0, len(temp_lst))))
    t2 = timeit.default_timer()
    elapsed = t2 - t1
    print(f"Time for remove operation, {size} times: " + str(elapsed) + "\n")
    print("------------------------- testing CLEAR -------------------------\n")
    if show:
        print(temp_lst)
    print("Clearing: ")
    t1 = timeit.default_timer()
    temp_lst.clear()
    t2 = timeit.default_timer()
    print(temp_lst)
    elapsed = t2 - t1
    print(f"Time for clear operation, 1 time: " + str(elapsed) + "\n")
    t_end = timeit.default_timer()
    print(f"All tests ran {t_end - t_start} seconds. ")


test_all_methods(200, 11, 5, -50, 50, False)

# create infinite loop which fetches elements one by one
# test how much memory
