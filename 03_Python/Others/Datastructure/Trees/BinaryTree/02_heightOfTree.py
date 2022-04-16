class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:

    def height(self, root):
        if root == None:
            return 0

        return max(self.height(root.left), self.height(root.right))+1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

tree = Tree()
print(tree.height(root))
