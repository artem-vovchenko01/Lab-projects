class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

def convert_to_circular(list):
    if list.last_node:
        list.last_node.next = list.head

def print_last_node_points_to(list):
    last = list.last_node
    if last is None:
        print('List is empty!')
        return
    if last.next is None:
        print('Last node points to None')
    else:
        print('Last node points to element with data {}.'.format(last.next.data))

a_list = LinkedList()
data_list = input('Please enter the elements in the linked list: ').split()
for data in data_list:
    a_list.append(int(data))

print_last_node_points_to(a_list)

print('Converting linked list to a circular linked list...')
convert_to_circular(a_list)

print_last_node_points_to(a_list)


