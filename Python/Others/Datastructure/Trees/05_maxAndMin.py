class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Tree:

    minVal = 100000000
    maxVal = -1

    def minFunc(self, root):
        if root:
            if root.data < self.minVal:
                self.minVal = root.data

            self.minFunc(root.left)
            self.minFunc(root.right)
        return self.minVal

    def maxFunc(self, root):
        if root:
            if root.data > self.maxVal:
                self.maxVal = root.data
            self.maxFunc(root.left)
            self.maxFunc(root.right)

        return self.maxVal

    def maximumFunc(self, root):
        if (root == None):
            return self.maxVal

        return max(root.data, max(self.maximumFunc(root.left), self.maximumFunc(root.right)))


root = Node(10)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(1)
root.left.right = Node(100)

tree = Tree()
print(tree.minFunc(root))
print(tree.maxFunc(root))
print(tree.maximumFunc(root))
