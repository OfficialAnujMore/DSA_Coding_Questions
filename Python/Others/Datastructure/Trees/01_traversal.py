class Node:

    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


class traversal:

    def printPreOrder(self, root):
        if root:
            print(root.val, end=" ")

            self.printPreOrder(root.left)

            self.printPreOrder(root.right)

    def printInOrder(self, root):
        if root:
            self.printInOrder(root.left)

            print(root.val, end=" ")

            self.printInOrder(root.right)

    def printPostOrder(self, root):
        if root:
            self.printPostOrder(root.left)

            self.printPostOrder(root.right)

            print(root.val, end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
tra = traversal()
print("Preorder traversal of binary tree is")
tra.printPreOrder(root)
print("")

print("Inorder traversal of binary tree is")
tra.printInOrder(root)
print("")

print("Postorder traversal of binary tree is")
tra.printPostOrder(root)
print("")
