class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 1

        while r < len(prices):
            while prices[l] < prices[r]:
                maxProfit = max(maxProfit, prices[r] - prices[l])
                r += 1
                if r >= len(prices):
                    return maxProfit

            l = r
            r = l + 1

        return maxProfit         

