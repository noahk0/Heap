def findKthLargest(self, nums: List[int], k: int) -> int:
    heapify(nums)

    for _ in range(k, len(nums)):
        heappop(nums)

    return heappop(nums)
