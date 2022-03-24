class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BST:

    def insert(self, root, x):

        if root == None:
            return False
        # if root


bst = BST()
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)
root.right.left = Node(25)
root.right.right = Node(40)

print(bst.insert(root, 45))
