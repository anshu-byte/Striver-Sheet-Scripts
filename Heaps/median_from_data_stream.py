from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):  # Store the lower half
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        heappush(self.maxheap, -num)
        maxHeapTop = -heappop(self.maxheap)
        heappush(self.minheap, maxHeapTop)

        if len(self.minheap) > len(self.maxheap):
            minHeapTop = heappop(self.minheap)
            heappush(self.maxheap, -minHeapTop)

    def findMedian(self) -> float:
        if len(self.minheap) == len(self.maxheap):
            return (self.minheap[0] + (-self.maxheap[0])) / 2
        else:
            return -self.maxheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
