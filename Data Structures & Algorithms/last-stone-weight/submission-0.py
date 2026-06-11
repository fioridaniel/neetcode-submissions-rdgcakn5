class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)
            diff = y - x
            
            if diff > 0:
                heapq.heappush_max(stones, diff)
        
        if len(stones) == 1:
            return stones[0]
        return 0