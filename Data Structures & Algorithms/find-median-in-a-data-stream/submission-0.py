class MedianFinder:

    def __init__(self):
        self.minHeap = [] ## for the larger half
        self.maxHeap = [] ## for the smaller half
        

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush_max(self.maxHeap, num)
        
        if len(self.minHeap) > len(self.maxHeap) + 1:
            val = heapq.heappop(self.minHeap)
            heapq.heappush_max(self.maxHeap, val)
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = heapq.heappop_max(self.maxHeap)
            heapq.heappush(self.minHeap, val)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (self.maxHeap[0] + self.minHeap[0]) / 2.0
        