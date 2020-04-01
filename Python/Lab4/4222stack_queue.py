""" 
Цей модуль містить реалізації абстрактних типів даних "черга" та "стек"
"""

class Stack:
    """
    Реалізація АТД стек
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

class Queue:
    """
    Реалізація АТД черга
    """
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

def _test():
    # Тести
    s = Stack()

    print("Stack: \n")
    s.push(5)
    s.push(10)
    print(s.is_empty())
    print(s.pop())
    print("\n")

    print("Queue: \n")
    q = Queue()
    print(q.isEmpty())
    q.enqueue(4)
    print(q.size())
    q.enqueue(8)
    print(q.dequeue())

if __name__ == "__main__":
    _test()