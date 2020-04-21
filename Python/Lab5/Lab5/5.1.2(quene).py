class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Quene:
    def __init__(self):
        self.head = None
        self.last = None

    def enquene(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def dequene(self):
        if self.head is None:
            return None
        else:
            to_return = self.head.data
            self.head = self.head.next
            return to_return

a_quene = Quene()
while True:
    print('enquene <value>')
    print('dequene')
    print('quit')
    do = input('What would you choose to do? ').split()

    operation = do[0].strip().lower()
    if operation == 'enquene':
        a_quene.enquene(int(do[1]))
    elif operation == 'dequene':
        dequened = a_quene.dequene()
        if dequened is None:
            print('Quene is empty!')
        else:
            print('Dequened element: ', int(dequened))
    elif operation == 'quit':
        break