class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Tree:

    def common(self,root,a,b):
        if root is None:
            return 

        if root.data == a or root.data == b:
            return root.data
       
        l = self.common(root.left, a,b)
        r = self.common(root.right, a,b)

        if (l == None): return r
        if (r == None): return l

        return root.data




root = Node(5)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.right = Node(1)
root.left.left.right.left = Node(7)
root.left.left.right.right = Node(6)

tree = Tree()
a = 4
b = 6

# print(tree.traverseTree(root))
print(tree.common(root,a,b))
