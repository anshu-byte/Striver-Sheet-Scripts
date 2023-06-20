# Definition for singly-linked list.
class ListNode:
    def __init__(self, x,next =None):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(headA, headB):
        d1 = headA
        d2 = headB

        while d1 != d2:
            d1 = headB if d1 is None else d1.next
            d2 = headA if d2 is None else d2.next
        return d1
    def printList(self,head):
        while head is not None:
            print(head.val,end=" ")
            head = head.next
        print()
    

            


        