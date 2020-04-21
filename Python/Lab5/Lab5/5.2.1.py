class Tree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def compare(self, new_value):
        if new_value >= self.value:
            if self.right:
                self.right.compare(new_value)
            else:
                self.right = Tree(new_value)

        if new_value < self.value:
            if self.left:
                self.left.compare(new_value)
            else:
                self.left = Tree(new_value)

    def sort(self):
        if self.left:
            self.left = self.left.sort()
        else:
            self.left = []

        if self.right:
            self.right = self.right.sort()
        else:
            self.right = []

        return self.left + [self.value] + self.right
class SortedTree():
    def __init__(self):
        self.root = None
    def push(self, value):
        if self.root:
            self.root.compare(value)
        else:
            self.root = Tree(value)
    def merge(self):
        return self.root.sort()


items = [7, 4, 2, 3, 8, 9, 10]
tree = SortedTree()
for value in items:
    tree.push(value)

print(tree.merge())


