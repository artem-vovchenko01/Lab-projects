import random
import timeit

class DoublyLinkedListIterator:
    def __init__(self, dList):
        self.__list = dList
        self.__idx = 0
        self.__size = len(dList)

    def __next__(self):
        if self.__idx < self.__size:
            i = self.__idx
            self.__idx += 1
            return self.__list.get(i)
        raise StopIteration

class Node:
    """Class which represents a node in a doubly-linked list"""

    def __init__(self, value):
        """Node initialization"""
        self.next = None
        self.prev = None
        self.val = value

class DoublyLinkedList:
    """Class which represents a doubly-linked list and incorporates various interfaces to work with it"""

    def __iter__(self) -> DoublyLinkedListIterator:
        """Get iterator object of this list"""
        return DoublyLinkedListIterator(self)

    def __init__(self, initial=None) -> None:
        """List initialization"""
        self.__index_exc = "Index should be in range from 0 to (list length - 1)"
        self.__zero_len = "List is of len 0"
        self.__not_all_nums = "Not all list elements are numbers. "
        temp = Node(None)
        self.__head = temp
        self.__tail = temp
        self.__size = 0
        if initial:
            try:
                temp = iter(initial)
                for el in initial:
                    self.add(el)
            except:
                pass

    def __str__(self) -> str:
        """String representation"""
        obj = self.__head.next
        string = "["
        while not (obj is None):
            string += obj.val.__str__()
            if obj.next is not None:
                string += ", "
            obj = obj.next
        return string + "]"

    def __len__(self) -> int:
        """Use len(list_name) to get list size"""
        return self.__size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.sub(key, value)

    def __contains__(self, value):
        return self.search(value)

    def __reversed__(self):
        return self.get_reversed()

    def add(self, val) -> None:
        """Add element to the end"""
        temp = Node(val)
        temp.prev = self.__tail
        self.__tail.next = temp
        self.__tail = temp
        self.__size += 1

    def insert(self, index : int, val) -> None:
        """Insert element under given index in range from 0 to list-length"""
        sz = self.__size
        if index < 0 or index > sz:
            raise Exception(self.__index_exc)
        if index > sz / 2:
            obj = self.__tail
            count = sz
            while count != index:
                obj = obj.prev
                count -= 1
        else:
            obj = self.__head
            count = 0
            while count != index:
                obj = obj.next
                count += 1
        if obj is self.__tail:
            temp = self.__tail
            new = Node(val)
            new.prev = self.__tail
            self.__tail = new
            temp.next = self.__tail
        else:
            temp = obj.next
            new = Node(val)
            new.prev = obj
            new.next = temp
            obj.next = new
            temp.prev = new
        self.__size += 1

    def rem_last(self) -> None:
        """Remove last element"""
        if self.__size > 0:
            obj = self.__tail
            obj.prev.next = None
            self.__tail = obj.prev
            del obj
        else:
            raise Exception(self.__zero_len)
        self.__size -= 1

    def remove(self, index : int) -> None:
        """Remove element by given index"""
        sz = self.__size
        if index < 0 or index >= sz:
            raise Exception(self.__index_exc)
        if index > sz / 2:
            obj = self.__tail
            count = sz - 1
            while count != index:
                obj = obj.prev
                count -= 1
        else:
            obj = self.__head.next
            count = 0
            while count != index:
                obj = obj.next
                count += 1
        if not obj == self.__tail:
            obj.prev.next = obj.next
            obj.next.prev = obj.prev
        else:
            obj.prev.next = None
            self.__tail = obj.prev
        del obj
        self.__size -= 1

    def sub_last(self, val) -> None:
        """Substitute the val of the last element"""
        if self.__size > 0:
            self.__tail.val = val
        else:
            raise Exception(self.__zero_len)

    def sub(self, index : int, val) -> None:
        """Substitute the val of the element by given index"""
        sz = self.__size
        if index < 0 or index >= sz:
            raise Exception(self.__index_exc)
        if index > sz / 2:
            obj = self.__tail
            count = sz - 1
            while count != index:
                obj = obj.prev
                count -= 1
        else:
            obj = self.__head.next
            count = 0
            while count != index:
                obj = obj.next
                count += 1
        obj.val = val

    def get_sum(self) -> int:
        """Calculate a sum of elements. Raises an Exception if not
         all elements are numbers. Returns None if the list is of 0 length"""
        result = 0
        obj = self.__head.next
        while obj is not None:
            try:
                result += float(obj.val)
            except:
                raise Exception(self.__not_all_nums)
            obj = obj.next
        if self.__size == 0:
            raise Exception(self.__zero_len)
        else:
            return result

    def find(self, val) -> int:
        """Returns the index of the first occurence of given val"""
        obj = self.__head
        index = -1
        while obj != self.__tail:
            obj = obj.next
            index += 1
            if obj.val == val:
                return index
        return None

    def find_all(self, val) -> list:
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

    def search(self, val) -> bool:
        """
        Returns True if val is present in list, else False
        """
        obj = self.__head
        while obj:
            if obj.val == val:
                return True
            obj = obj.next
        return False

    def get(self, index : int):
        """Returns the value contained under given index"""
        sz = self.__size
        if index < 0 or index >= sz:
            raise Exception(self.__index_exc)
        if index > sz / 2:
            obj = self.__tail
            count = sz - 1
            while count != index:
                obj = obj.prev
                count -= 1
        else:
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

    def clear(self) -> None:
        """Clears the list"""
        while self.__size > 0:
            self.rem_last()

    def get_reversed(self):
        """Returns reversed DoublyLinkedList"""
        obj = self.__tail
        lst = DoublyLinkedList()
        while obj != self.__head:
            lst.add(obj.val)
            obj = obj.prev
        return lst

class DoublyLinkedListTester:
    @staticmethod
    def test_all_methods(size, find, insertions, low_val, high_val, show):
        t_start = timeit.default_timer()
        temp_lst = DoublyLinkedList()
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
