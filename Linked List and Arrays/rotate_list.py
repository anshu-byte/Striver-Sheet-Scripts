# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head,k):
        if head == None or head.next == None or k == 0:
            return head
        # calculating length
        temp = head
        length = 1
        while temp.next != None:
            length += 1
            temp = temp.next
        temp.next = head
        k = k%length
        for i in range(length-k-1):
            head = head.next
        res = head.next
        head.next = None
        return res



        
