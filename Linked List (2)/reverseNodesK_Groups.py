# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseLinkedList(
        self, begin: Optional[ListNode], end: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev = None
        while begin != end:
            next_ = begin.next
            begin.next = prev
            prev = begin
            begin = next_
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1 or head is None or head.next is None:
            return head

        dummy = ListNode(0, head)
        back, forward = dummy, head

        while True:
            groupLen = 0
            while groupLen < k and forward:
                forward = forward.next
                groupLen += 1

            if groupLen != k:
                break

            last = back.next

            back.next = self.reverseLinkedList(back.next, forward)

            last.next = forward
            back = last

        return dummy.next
