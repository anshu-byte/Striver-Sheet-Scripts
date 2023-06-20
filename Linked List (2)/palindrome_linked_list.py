# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        # edge case
        if head == None or head.next == None:
            return True

        # find mid node
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        # reverse after mid nodes
        prev,curr,next = None,slow.next,None
        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        slow.next = prev

        # now compare from start and after mid elements
        dummy = head
        slow = slow.next
        while slow != None:
            print(dummy.val,slow.val)
            if dummy.val != slow.val:
                return False
            dummy = dummy.next
            slow = slow.next
        return True
        
sol = Solution()
head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
print(sol.isPalindrome(head))