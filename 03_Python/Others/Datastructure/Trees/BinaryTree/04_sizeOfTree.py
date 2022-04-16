class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Tree:

    def size(self, root):
        if root == None:
            return 0
        return self.size(root.left) + self.size(root.right) +1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

tree = Tree()
print(tree.size(root))
