class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BST:

    def search(self, root, x):

        if root == None:
            return False

        if root.data == x:
            return True
        if root.data > x:
            return self.search(root.left, x)

        return self.search(root.right, x)


bst = BST()
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)
root.right.left = Node(25)
root.right.right = Node(40)

print(bst.search(root, 40))
