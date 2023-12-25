from collections import deque


class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # push operation costly
        # self.q2.append(x)
        # while self.q1:
        #     self.q2.append(self.q1.popleft())
        # self.q2, self.q1 = self.q1, self.q2

        # pop operation costly
        self.q1.append(x)

    def pop(self) -> int:
        # push operation costly
        # if self.empty():
        #     return None
        # else:
        #     return self.q1.popleft()

        # pop operation costly
        if self.empty():
            return None

        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        popped_element = self.q1.popleft()

        self.q1, self.q2 = self.q2, self.q1

        return popped_element

    def top(self) -> int:
        if self.empty():
            return None
        else:
            # push operation costly
            # return self.q1[0]

            # pop operation costly
            return self.q1[-1]

    def empty(self) -> bool:
        return not self.q1
