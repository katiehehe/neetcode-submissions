class MedianFinder:

    def __init__(self):
        self.bottom = []
        self.top = []

    def addNum(self, num: int) -> None:
        # push onto a pq
        if len(self.top) == 0 or num >= self.top[0]:
            heapq.heappush(self.top, num)
        else:
            heapq.heappush(self.bottom, -num)
        # fix the size
        if len(self.bottom) == 1 + len(self.top):
            elem = -heapq.heappop(self.bottom)
            heapq.heappush(self.top, elem)
        elif len(self.top) == 2 + len(self.bottom):
            elem = heapq.heappop(self.top)
            heapq.heappush(self.bottom, -elem)

    def findMedian(self) -> float:
        if len(self.top) == 1 + len(self.bottom):
            return self.top[0]
        return (self.top[0] - self.bottom[0]) / 2
        
        