from turtle import pos


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print("")

    # O(1)

    def pushAtFirst(self, data):
        data = Node(data)
        data.next = self.head
        self.head = data

    def pushAtN(self, prev_node, new_data):
        # headNode = self.head

        if (prev_node < 1):
            print("Invaid")

        if prev_node == 1:
            newNode = Node(new_data)
            newNode.next = self.head
            self.head = newNode
        else:
            while (prev_node != 0):
                prev_node -= 1

                if prev_node == 1:
                    newNode = Node(new_data)
                    newNode.next = self.head.next
                    self.head.next = newNode
                    break

                self.head = self.head.next

                if self.head == None:
                    print('Position out of range')

    def pushAtNth(self, prev_node, new_data):
        if prev_node == None:
            print('Invalid')
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def delete(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:  # 8
                break
            prev = temp  # 12 1 2 128
            temp = temp.next  # 1 2 128 8

        if (temp == None):
            return
        prev.next = temp.next  # 128 -> 3
        temp = None

    def deleteAtNth(self, position):


        if self.head is None:
            return

        if position == 0:
            self.head= self.head.next
            return self.head

        index = 0
        current = self.head
        prev = self.head
        temp = self.head

        while temp is not None:
            if index == position:
                temp = current.next
                break
            else:
                prev = current
                current = current.next
                index+=1
        prev.next = temp
        return prev
    


if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.pushAtFirst(12)

    llist.pushAtNth(second, 8)
    llist.pushAtNth(second, 128)
    llist.append(128)

    llist.printList()
    llist.delete(8)
    llist.printList()
    llist.deleteAtNth(3)
    llist.printList()
