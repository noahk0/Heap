class MedianFinder:

    def __init__(self):
        self.low, self.high = [], []

    def addNum(self, num: int) -> None:
        if len(self.low) == len(self.high):
            heappush(self.high, -heappushpop(self.low, -num))
        else:
            heappush(self.low, -heappushpop(self.high, num))

    def findMedian(self) -> float:
        return self.high[0] if len(self.low) < len(self.high) else (self.high[0] - self.low[0]) / 2
