class Node:
    def __init__(self, row = None, next = None):
        self.row = row
        self.next = next
        
    def __str__(self):
        return self.row.__str__()

class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        if self.head != None:
            temp = self.head
            rez = "Hash Table via Single Linked List : " + str(temp)
            while temp.next != None:
                temp = temp.next
                rez += ", " + str(temp)
            return rez
        else:
            return 'Hash Table is empty'
        
    def search(self, key):
        temp = self.head
        if temp is None:
            return None
        while temp.next is not None:
            if temp.row.key == key:
                return temp
            temp = temp.next
        if temp.next is None and temp.row.key == key:
            return temp          
        return None
                
    def clear(self):
        self.__init__()
        
    def add(self, row):
        temp = self.head
        if temp is None:
            self.head = Node(row, None)
            return
        self.head = Node(row, self.head)
        return
    
    def rem(self, key):
        temp = self.head
        if temp is None:
            return
        if temp.row.key == key:
            self.head = Node(temp.next.row, temp.next.next)
        while temp.next is not None:
            old = temp
            temp = temp.next
            if temp.row.key == key:
                old.next = temp.next
        return
        
    def full(self, string):
        arr = string.split()
        for i in arr:
            self.add(i)


class HashRow:
    def __init__(self, key, val):
        self.key = self.HashKey(key)
        self.val = val
        
    def HashKey(self, key):
        temp = str(key)
        summary = 0
        for i in range(len(temp)):
            summary += ord(temp[i])*i*37
        return summary
    
    def __str__(self):
        return self.val

class HashTable:
    def __init__(self):
        self.table = SLL()
        self.size = 0
                
    def add(self, phone, street, city):
        row = HashRow(phone, city + " " + street)
        if self.duplicate(row.key):
            self.search(phone).row.val = row.val
        else:
            self.table.add(row)
            self.size += 1
            
    def __str__(self):
        return self.table.__str__()
    
    def duplicate(self, key):
        temp = self.table.head
        if temp is None:
            return False
        while temp.next is not None:
            if temp.row.key == key:
                return True
            temp = temp.next
        if temp.next == None and temp.row.key == key:
                return True
        return False
    
    def search(self, key):
        temp = HashRow(key, "")
        return self.table.search(temp.key)
    
    def remove(self, key):
        temp = HashRow(key, "")
        return self.table.rem(temp.key)
        
    def create(self, size):
        phone = 380501112233
        for i in range(size):
            phone += 1
            row = HashRow(phone, "City Street")
            self.table.add(row)
            self.size += 1
            
    def testing(self):
        for size in [1000, 10000, 100000, 200000]:
            crt_time = datetime.now()
            self.__init__()
            self.create(size)
            print(self.size)
            print("Time for creating Hash Table of", size, ":", datetime.now()-crt_time)
            srch_time = datetime.now()
            search = 380501112233
            for search in range(search, search + 500, 1):
                if not self.search(search):
                    print("Error")
            print("Time for searching 500 elements in Hash Table of", size, ":", datetime.now()-srch_time)
        
from datetime import datetime

H = HashTable()
H.add(1235, "Peremogu", "Kyiv")
H.add(1235, "Mazepa", "Kyiv")
H.add(1245, "Ozerna", "Piter")
H.add(1355, "Sad", "Omsk")
print(H)
print(H.search(1355))
H.remove(1235)
print(H)
S = HashTable()
S.create(5)
print(S)