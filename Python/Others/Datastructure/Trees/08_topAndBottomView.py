class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.hd = 0


class Tree:

    def topView(self, root):
        queue = []
        m = dict()
        hd = 0
        root.hd = hd
        queue.append(root)

        while (len(queue)):
            root = queue[0]
            hd = root.hd

            if hd not in m:
                m[hd] = root.data

            if root.left:
                root.left.hd = hd-1
                queue.append(root.left)
            if root.right:
                root.right.hd = hd+1
                queue.append(root.right)

            queue.pop(0)
        print(m)
        for i in sorted(m):
            print(m[i], end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)
print("Following are nodes in top",
      "view of Binary Tree")
tree = Tree()
tree.topView(root)
