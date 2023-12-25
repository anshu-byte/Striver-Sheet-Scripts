from collections import deque


class MyQueue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def push(self, x: int) -> None:
        self.s1.append(x)

    def move_elements(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

    def pop(self) -> int:
        if self.empty():
            return None
        self.move_elements()
        return self.s2.pop()

    def peek(self) -> int:
        if self.empty():
            return None
        self.move_elements()
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2
