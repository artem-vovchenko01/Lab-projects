class Node:
    def __init__(self, data, color, parent, left=None, right=None):
        self.data = data
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

class RedBlackTree:
    def __init__(self, root=None):
        self.__BLACK = "black"
        self.__RED = "red"
        self.__root = Node(root, self.__BLACK, None)

    def rebalance(self, node):
        while node.parent.color == self.__RED:
            p = node.parent
            gp = node.parent.parent
            if gp.left == p:
                uncle = gp.right
            else:
                uncle = gp.left
            if uncle.color == self.__RED:
                gp.color = self.__RED
                p.color = uncle.color = self.__BLACK
                node = gp

    def insert(self, data):
        root = self.__root
        if root is None:
            self.__root = Node(data, self.__BLACK, None)
            return
        while root is not None:
            if data == root.data:
                node = root
                break
            if data > root.data:
                if root.right is not None:
                    root = root.right
                else:
                    node = Node(data, self.__RED, root)
                    root.right = node
                    break
            if data < root.data:
                if root.left is not None:
                    root = root.left
                else:
                    node = Node(data, self.__RED, root)
                    root.left = node

        self.rebalance(node)

"""
Not Finished
"""