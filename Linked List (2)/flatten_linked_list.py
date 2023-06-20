class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
def mergeTwoLists2(list1,list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.data>list2.data:
            list1,list2 = list2,list1
        res = list1
        while list1!= None and list2!= None:
            prev = None
            while list1!=None and list1.data<=list2.data:
                prev = list1
                list1 = list1.bottom
            prev.bottom = list2
            list1,list2 = list2,list1
        return res
def flatten(root):
    #Your code here
    if root.next==None:
        return root
    res = flatten(root.next)
    res = mergeTwoLists2(res,root)
    return res
def printList(head):
    while head is not None:
        print(head.data,end=" ")
        head = head.bottom
    print()
# Test case 1
list1 = Node(5)
list1.bottom = Node(7)
list1.bottom.bottom = Node(8)
list1.bottom.bottom.bottom = Node(30)
list2 = Node(10)
list2.bottom = Node(20)
list3 = Node(19)
list3.bottom = Node(22)
list3.bottom.bottom = Node(50)
list4 = Node(28)
list4.bottom = Node(35)
list4.bottom.bottom = Node(40)
list4.bottom.bottom.bottom = Node(45)
list1.next = list2
list2.next = list3
list3.next = list4
res_list = flatten(list1)
printList(res_list)