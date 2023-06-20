# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, k):
        # # len(list) - n from start
        # n = 0
        # temp = head
        # while temp!=None:
        #     n += 1
        #     temp = temp.next
        # if n==1 and k==1:
        #     return None
        # if n==k:
        #     return head.next
        # prev = None
        # curr = None
        # res = head
        # for i in range(n-k):
        #     prev = head
        #     curr = head.next
        #     head = head.next
        # prev.next = curr.next
        # curr.next  = None
        # return res

        # optimized approach
        start = ListNode()
        start.next = head
        fast = start
        slow = start

        for _ in range(k):
            fast = fast.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return start.next
        
        


    def printList(self,head):
        while head is not None:
            print(head.val,end=" ")
            head = head.next
        print()
sol = Solution()
list1 = ListNode(1)
# list1.next = ListNode(2)
# list1.next.next = ListNode(3)
# list1.next.next.next = ListNode(4)
# list1.next.next.next.next = ListNode(5)
res_list = sol.removeNthFromEnd(list1,1)
sol.printList(res_list)
        



