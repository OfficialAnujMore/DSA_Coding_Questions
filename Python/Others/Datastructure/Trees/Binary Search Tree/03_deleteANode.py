from bisect import insort


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BST:

    def delete(self, root, nodeToDelete):

        if root is None:
            return root

        if root.data == nodeToDelete:
            print('found')

        if nodeToDelete < root.data:
            root.left = self.delete(root.left, nodeToDelete)
        elif (nodeToDelete > root.data):
            root.right = self.delete(root.right, nodeToDelete)

        return root

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.data, end=' ')
            self.inOrder(root.right)


bst = BST()
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)

bst.delete(root, 30)
bst.inOrder(root)
