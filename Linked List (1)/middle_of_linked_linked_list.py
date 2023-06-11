# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    def lengthOfList(self,head):
        cnt = 0
        while head is not None:
            head = head.next
            cnt += 1
        return cnt
    def middleNode(self, head):
        cnt = self.lengthOfList(head)
        midIndex = cnt//2
        cnt = 0
        while cnt<midIndex:
            head = head.next
            cnt += 1
        return head
    # Tortoise-Hare-Approach
    def middleNode2(self,head):
        slow,fast = head,head
        while fast:
            slow = slow.next
            fast = fast.next.next
        return slow

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
# head = sol.middleNode(head)
head = sol.middleNode2(head)
sol.printList(head)








