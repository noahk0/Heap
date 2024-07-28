def lastStoneWeight(self, stones: List[int]) -> int:
    stones = [- stone for stone in stones]
    heapify(stones)

    while 1 < len(stones):
        heappush(stones, heappop(stones) - heappop(stones))

    return - stones[0]
