class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_k = max(piles)

        while l <= r:
            k = (l + r) // 2

            curr_h = 0
            for i in range(len(piles)):
                curr_h += -(-piles[i] // k)
            
            if curr_h <= h:
                min_k = min(min_k, k)
                r = k - 1
            else:
                l = k + 1

        return min_k
