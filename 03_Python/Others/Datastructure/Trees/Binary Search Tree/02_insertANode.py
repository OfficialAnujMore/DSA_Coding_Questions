from bisect import insort


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BST:

    def insert(self, root, x):
        if root == None:
            return Node(x)
        else:
            if root.data == x:
                return root
            elif root.data > x:
                root.left = self.insert(root.left, x)
            else:
                root.right = self.insert(root.right, x)

        return root

    def insertIteratively(self,root,x):
        newNode = Node(x)
        cur = root
        parent = None

        while (cur!=None):
            parent = cur
            if (x < cur.data):
                cur = cur.left
            else:
                cur = cur.right

        if parent == None:
            parent = newNode
        elif (x < parent.data):
            parent.left = newNode
        else:
            parent.right = newNode

        return parent


    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.data, end = ' ')
            self.inOrder(root.right)

bst = BST()
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)

bst.insert(root, 33)
bst.inOrder(root)
print()
print("------------")
bst.insertIteratively(root, 66)
bst.inOrder(root)
