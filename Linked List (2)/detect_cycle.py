# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        if head==None:
            return False
        s,f = head,head
        while s.next!=None and f.next!=None and f.next.next!=None:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False
    def printList(self,head):
        while head is not None:
            print(head.val,end=" ")
            head = head.next
        print()
sol = Solution()
# list1 = ListNode(2)
# list1.next = ListNode(4)
# list1.next.next = ListNode(3)
# list1.next.next.next = list1.next
list1 = None
res_list = sol.hasCycle(list1)
print(res_list)