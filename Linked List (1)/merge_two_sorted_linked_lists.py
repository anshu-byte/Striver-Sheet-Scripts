# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # with extra space
    # def mergeTwoLists(self, list1, list2):
    #     res = ListNode(0)
    #     curr = res
    #     while list1 and list2:
    #         if list1.val <= list2.val:
    #             curr.next = ListNode(list1.val)
    #             list1 = list1.next
    #         else:
    #             curr.next = ListNode(list2.val)
    #             list2 = list2.next
    #         curr = curr.next
    #     print(curr.val)
    #     curr.next = list1 or list2
    #     return res.next

    # Without extra space - inplace method
    def mergeTwoLists2(self,list1,list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val>list2.val:
            list1,list2 = list2,list1
        res = list1
        while list1!= None and list2!= None:
            prev = None
            while list1!=None and list1.val<=list2.val:
                prev = list1
                list1 = list1.next
            prev.next = list2
            list1,list2 = list2,list1
        return res


    def printList(self,head):
        while head is not None:
            print(head.val,end=" ")
            head = head.next
        print()
sol = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
# res_list = sol.mergeTwoLists(list1,list2)
res_list = sol.mergeTwoLists2(list1,list2)
sol.printList(res_list)


        




        
