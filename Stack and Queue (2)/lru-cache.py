from collections import deque


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.order = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            self.order.remove(key)
            self.order.appendleft(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
            self.order.appendleft(key)
            self.cache[key] = value
        else:
            if len(self.order) == self.capacity:
                removed_key = self.order.pop()
                del self.cache[removed_key]
            self.cache[key] = value
            self.order.appendleft(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
