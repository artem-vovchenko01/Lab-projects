import random
import timeit

class Node:
    """
    Node element for BinarySearchTree()
    """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinarySearchTree:
    """
    Tree without balancing
    """
    def __init__(self):
        """
        Initializing empty tree 
        """
        self.__root = None

    def __str__(self):
        """
        Returns string representation of a tree in the form of set
        """
        string = "{"
        if not self.__root:
            return string + "}"
        level = [self.__root]
        nextlevel = []
        queue = []
        while level:
            queue.extend(level)
            for el in level:
                if el.left is not None: nextlevel.append(el.left)
                if el.right is not None: nextlevel.append(el.right)
            level = nextlevel
            nextlevel = []
        for el in queue:
            string += f"{el.data}, "
        return string[:-2] + "}"

    def get_list (self):
        """
        Returns list with all tree's elements
        """
        if not self.__root:
            return []
        level = [self.__root]
        nextlevel = []
        queue = []
        while level:
            queue.extend(level)
            for el in level:
                if el.left is not None: nextlevel.append(el.left)
                if el.right is not None: nextlevel.append(el.right)
            level = nextlevel
            nextlevel = []
        return [el.data for el in queue]

    def add_all(self, lst):
        """
        Adds all elements from given list to the tree
        """
        for el in lst:
            self.add(el)

    def raw_search(self, key):
        """
        Searches node by given key, returns the node object
        """
        return self.__raw_search_rec(key, self.__root)

    def __raw_search_rec(self, key, root):
        """
        Helping recursive function for raw_search
        """
        if root is None or root.data == key:
            return root
        if key > root.data:
            return self.__raw_search_rec(key, root.right)
        if key < root.data:
            return self.__raw_search_rec(key, root.left)

    def search(self, key):
        """
        Searches node by given key, returns True if found, else False
        """
        if self.raw_search(key) is None:
            return False
        else:
            return True
        
    def add(self, data):
        """
        Adds element to the tree
        """
        elem = self.__root
        if elem == None:
            self.__root = Node(data)
            return
        while True:
            if data > elem.data:
                if elem.right != None:
                    elem = elem.right
                else:
                    elem.right = Node(data)
                    break
            if data < elem.data:
                if elem.left != None:
                    elem = elem.left
                else:
                    elem.left = Node(data)
                    break
            if data == elem.data:
                break

    def get_parent (self, node):
        """
        Returns parent object of given node. None if node is not present in the tree
        """
        result = None
        def search(root):
            nonlocal result
            if root.left == node or root.right == node:
                result = root
            if root.left is not None:
                search(root.left)
            if root.right is not None:
                search(root.right)
        if self.__root is None:
            return None
        search(self.__root)
        return result

    def find_min(self, node):
        """
        Returns the node with minimum value from passed node's subtree (including passed node)
        """
        if node.left:
            return self.find_min(node.left)
        else:
            return node

    def remove(self, data): 
        """
        Removes first found element with given key. Returns True if removed, False if not found
        """
        el = self.raw_search(data)
        def internal_remove(root, el):
            parent = self.get_parent(el)
            right_parent = (parent.right == el)
            # if leaf
            if (not el.right) and (not el.left):
                if right_parent:
                    parent.right = None
                    del el
                    return True
                else:
                    parent.left = None
                    del el
                    return True
            # if has 2 children
            elif el.right and el.left:
                right_min = self.find_min(el.right)
                el.data = right_min.data
                right_min_parent = self.get_parent(right_min)
                internal_remove(right_min_parent, right_min)
                return True
            # if has 1 child
            else:
                if right_parent:
                    if el.right:
                        parent.right = el.right
                        del el
                        return True
                    else:
                        parent.right = el.left
                        del el
                        return True
                else:
                    if el.right:
                        parent.left = el.right
                        del el
                        return True
                    else:
                        parent.left = el.left
                        del el
                        return True
        # if tree is empty or el not in the tree
        if (not self.__root) or (not el):
            return False
        # if el is ROOT
        if el == self.__root:
            # 1 or no child
            if not el.right:
                self.__root = el.left
            elif not el.left:
                self.__root = el.right
             # if has 2 children
            else:
                right_min = self.find_min(el.right)
                el.data = right_min.data
                right_min_parent = self.get_parent(right_min)
                internal_remove(right_min_parent, right_min)
                return True
            del el 
            return True
        return internal_remove(self.__root, el)

def test_binary_tree (size, low_val, high_val, show = False):
    t_start = timeit.default_timer()
    print("------------------------- testing ADD -------------------------\n")
    tree1 = BinarySearchTree()
    print(f"Adding {size} elements in range from 0 to {size}: ")
    temp_lst1 = [i for i in range(size)]
    t1 = timeit.default_timer()
    tree1.add_all(temp_lst1)
    t2 = timeit.default_timer()
    elapsed = t2 - t1
    if show:
        print(tree1)
    print(f"Time for add operation, elements in order, {size} times: " + str(elapsed) + "\n")

    tree2 = BinarySearchTree()
    print(f"Adding {size} elements in range from {low_val} to {high_val}: ")
    temp_lst2 = [random.randint(low_val, high_val) for i in range(size)]   
    t1 = timeit.default_timer()
    tree2.add_all(temp_lst2)
    t2 = timeit.default_timer()
    elapsed = t2 - t1
    if show:
        print(tree2)
    print(f"Time for add operation, random elements, {size} times: " + str(elapsed) + "\n")

    print("------------------------- testing SEARCH -------------------------\n")
    print(f"Searching {size} elements in range from {low_val} to {high_val}: ")
    temp_lst3 = [random.randint(low_val, high_val) for i in range(size)]
    t1 = timeit.default_timer()
    for el in temp_lst3:
        tree2.search(el)
    t2 = timeit.default_timer()
    elapsed = t2 - t1

    print(f"Time for search operation, random elemetns, {size} times: " + str(elapsed) + "\n")

    print("------------------------- testing REMOVE -------------------------\n")
    print(f"Removing all elements from tree: ")
    temp_lst4 = tree2.get_list()

    t1 = timeit.default_timer()
    for el in temp_lst4:
        tree2.remove(el)
    t2 = timeit.default_timer()
    elapsed = t2 - t1
    print(f"Tree now: {tree2.__str__()}")
    print(f"Time for remove operation, {size} times: " + str(elapsed) + "\n")
    t_finish = timeit.default_timer()
    print(f"Time for all operations: " + str(t_finish) + "\n")

print()
test_binary_tree(1_000, -100_000, 100_000, False)