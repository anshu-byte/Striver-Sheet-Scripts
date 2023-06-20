# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        if head==None:
            return None
        s,f = head,head
        while s.next!=None and f.next!=None and f.next.next!=None:
            s = s.next
            f = f.next.next
            if s == f:
                break
        if f.next==None or f.next.next==None:
            return None
        while s!=f:
            s = s.next
            f = f.next
        return s
    def printList(self,head):
        while head is not None:
            print(head.val,end=" ")
            head = head.next
        print()
