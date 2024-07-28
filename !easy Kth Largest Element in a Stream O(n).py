class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.stream = k, nums
        heapify(self.stream)

        for _ in range(k, len(nums)):
            heappop(self.stream)

    def add(self, val: int) -> int:
        heappush(self.stream, val)

        if self.k < len(self.stream):
            heappop(self.stream)

        return self.stream[0]
