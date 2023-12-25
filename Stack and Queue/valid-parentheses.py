from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        st = deque()
        for i in s:
            if not st:
                st.append(i)
            else:
                if i == ")" and st[-1] == "(":
                    st.pop()
                elif i == "}" and st[-1] == "{":
                    st.pop()
                elif i == "]" and st[-1] == "[":
                    st.pop()
                else:
                    st.append(i)
        return True if len(st) == 0 else False
