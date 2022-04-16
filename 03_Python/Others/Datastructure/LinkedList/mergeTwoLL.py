class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addToList(self, newData):
        newNode = ListNode(newData)
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = newNode
    def mergeTwoLists(self, l1,l2):

        dummyNode = ListNode(0)

        print("dummyNode", dummyNode, l1, l2)

        tail = dummyNode
        print("Tail", tail)

        while True:

            if l1 is None:
                tail.next = l2
            if l2 is None:
                tail.next = l1

            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next

            else:
                tail.next = l2
                l2 = l2.next

        print("Tail", tail)
        

sol = Solution()
listA = Solution()
listB = Solution()
  
# Add elements to the list in sorted order
listA.addToList(5)
listA.addToList(10)
listA.addToList(15)
  
listB.addToList(2)
listB.addToList(3)
listB.addToList(20)
  
# Call the merge function

listA.head = sol.mergeTwoLists(listA.head, listB.head)
  
# Display merged list
print("Merged Linked List is:")
listA.printList()