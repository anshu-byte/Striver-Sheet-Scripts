from collections import defaultdict, deque


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.counter = defaultdict(int)
        self.freq_map = defaultdict(deque)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self._update_frequency(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.cache:
            self.cache[key] = value
            self._update_frequency(key)
        else:
            self._handle_new_key(key, value)

    def _update_frequency(self, key: int) -> None:
        freq = self.counter[key]
        self._remove_key_from_freq_map(freq, key)

        if not self.freq_map[freq] and freq == self.min_freq:
            self.min_freq += 1

        freq += 1
        self.counter[key] = freq
        self.freq_map[freq].appendleft(key)

    def _remove_key_from_freq_map(self, freq: int, key: int) -> None:
        self.freq_map[freq].remove(key)

    def _handle_new_key(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity:
            self._evict_least_frequently_used()
        self.cache[key] = value
        self.counter[key] = 1
        self.freq_map[1].appendleft(key)
        self.min_freq = 1

    def _evict_least_frequently_used(self) -> None:
        freq = self.min_freq
        least_frequently_used_key = self.freq_map[freq].pop()
        del self.cache[least_frequently_used_key]
        del self.counter[least_frequently_used_key]
