class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        # Code here
        aux_stack = []
        while s:
            e = s.pop()
            while aux_stack and aux_stack[-1] < e:
                s.append(aux_stack.pop())
            aux_stack.append(e)
        while aux_stack:
            s.append(aux_stack.pop())
