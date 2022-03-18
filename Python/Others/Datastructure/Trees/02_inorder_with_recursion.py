class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class traversal:


    def printInorder(self,root):
        current = root
        stack = []
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif(stack):
                current = stack.pop()
                print(current.data, end=" ")
                current = current.right
            else:
                break

    print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inOrder = traversal()

inOrder.printInorder(root)



