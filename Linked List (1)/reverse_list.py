# Definition for singly-linked list.
class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self,head):
        prev,curr,next = None,head,None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    temp = None
    def reverseList2(self,head):
        if head.next is None:
            self.temp = head
            return
        self.reverseList2(head.next)
        q = head.next
        q.next = head
        head.next = None

    # recursive code for reversing the list
    def reverseListRecursive(self,head):
        if head is None or head.next is None:
            return head
        p = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        return p

    def reversePrint(self,head):
        if head is None:
            return
        self.reversePrint(head.next)
        print(head.val,end=" ")
    def printList(self,head):
        while head is not None:
            print(head.val,end=" ")
            head = head.next
        print()
sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
sol.printList(head)
# sol.reverseList2(head)
# sol.printList(sol.temp)
# print("Reverse print")
# sol.reversePrint(head)
sol.reverseList(head)
# print()
# head = sol.reverseListRecursive(head)
print("After reversing the list")
sol.printList(head)