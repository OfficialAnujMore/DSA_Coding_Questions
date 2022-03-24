class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Tree:
    # O(n^2)
    def height(self, root):
        if root is None:
            return 0

        return max(self.height(root.left), self.height(root.right)) + 1

    def diameter(self, root):
        if root is None:
            return 0
        lHeight = self.height(root.left)
        rHeight = self.height(root.right)

        lDiameter = self.diameter(root.left)
        rDiameter = self.diameter(root.right)

        return max(lHeight+rHeight+1, max(lDiameter, rDiameter))

    # Optimized solutions
    # O(n)

    def heightOpt(root,ans):
        if root is None:
            return
        lHeight = (root.left, ans)
        rHeight = (root.right, ans)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

tree = Tree()

# print(tree.traverseTree(root))
print(tree.diameter(root))
