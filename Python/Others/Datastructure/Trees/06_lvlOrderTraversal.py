import queue


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Tree:
    treeheight = 0
    queue = []
    # O(n^2)

    # def traversal(self, root, level):
    #     if root == None:
    #         return
    #     elif level == 1:
    #         print(root.data, end=" ")
    #     else:
    #         self.traversal(root.left, level-1)
    #         self.traversal(root.right, level-1)

    # def traverseTree(self, root):
    #     h = self.height(root)
    #     for lvl in range(1, h+1):
    #         print("TT ROOOT", root)
    #         self.traversal(root, lvl)

    # def height(self, root):
    #     if root == None:
    #         return 0

    #     return max(self.height(root.left), self.height(root.right))+1

    def queueTraversal(self, root):

        if root is None:
            return

        if len(self.queue) == 0:
            self.queue.append(root)

        if root.left is not None:
            self.queue.append(root.left)

        if root.right is not None:
            self.queue.append(root.right)

        if len(self.queue) > 0:
            print(self.queue[0].data, end=" ")
            self.queue.pop(0)
            if len(self.queue) == 0:
                return
            else:
                self.queueTraversal(self.queue[0])

    def queueTraversalNew(self, root):
        myQueue = []
        if root is None:
            return

        myQueue.append(root)

        while (len(myQueue) > 0):
            print(myQueue[0].data, end=' ')
            curNode = myQueue.pop(0)
            if curNode.left is not None:
                myQueue.append(curNode.left)

            if curNode.right is not None:
                myQueue.append(curNode.right)


root = Node(5)
root.left = Node(1)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(3)
root.right.right = Node(6)

tree = Tree()

# print(tree.traverseTree(root))
tree.queueTraversal(root)
print()
tree.queueTraversalNew(root)
