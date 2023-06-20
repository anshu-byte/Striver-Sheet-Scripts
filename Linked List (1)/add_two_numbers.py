# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        start = ListNode()
        curr = start
        carry = 0
        while l1!=None and l2!=None:
            check = l1.val + l2.val + carry
            carry = check//10
            val = check%10
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1!=None:
            check = l1.val + carry
            carry = check//10
            val = check%10
            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
        while l2!=None:
            check = l2.val + carry
            carry = check//10
            val = check%10
            curr.next = ListNode(val)
            curr = curr.next
            l2 = l2.next
        if carry!=0:
            curr.next = ListNode(carry)
        return start.next
    def printList(self,head):
        while head is not None:
            print(head.val,end=" ")
            head = head.next
        print()
sol = Solution()
list1 = ListNode(2)
list1.next = ListNode(4)
list1.next.next = ListNode(3)
list2 = ListNode(5)
list2.next = ListNode(6)
list2.next.next = ListNode(4)
res_list = sol.addTwoNumbers(list1,list2)
sol.printList(res_list)
