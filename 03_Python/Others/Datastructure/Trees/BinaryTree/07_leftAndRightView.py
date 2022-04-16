class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def leftViewUtils(self, root, level, max_level):
        if root == None:
            return
        if max_level[0] < level:
            print(root.data, end=" ")
            max_level[0] = level

        self.leftViewUtils(root.left, level+1, max_level)
        self.leftViewUtils(root.right, level+1, max_level)

    def leftView(self, root):
        max_level = [0]
        self.leftViewUtils(root, 1, max_level)

    def rightViewUtils(self, root, level, maxRightVal):
        if root == None:
            return

        if maxRightVal[0] < level:
            print(root.data, end=" ")
            maxRightVal[0] = level

        self.rightViewUtils(root.right, level+1, maxRightVal)
        self.rightViewUtils(root.left, level+1, maxRightVal)

    def rightView(self, root):
        maxRightVal = [0]
        self.rightViewUtils(root, 1, maxRightVal)


tree = Tree()

# RIGHT VIEW CHECKER
# root = Node(10)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(7)
# root.left.right = Node(8)
# root.right.right = Node(15)
# root.right.left = Node(12)
# root.right.right.left = Node(14)


# LEFT VIEW CHECKER
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)


tree.leftView(root)
print()
tree.rightView(root)
