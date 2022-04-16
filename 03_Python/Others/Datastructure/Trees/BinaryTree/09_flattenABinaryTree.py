
class Node:

    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class Tree:
    prev = Node(None)
    head = Node(None)

    def convertToDLL(self, root):
        if root == None:
            return
        self.convertToDLL(root.left)
        if self.prev == None:
            self.head = root
        else:
            root.left = self.prev
            self.prev.right = root
        self.prev = root

        self.convertToDLL(root.right)


root = Node(3)
root.left = Node(5)
root.right = Node(2)
root.right.left = Node(1)
root.right.left.left = Node(4)
root.right.left.right = Node(6)
tree = Tree()

tree.convertToDLL(root)
