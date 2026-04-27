class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxProfit = 0

        for r in range(len(prices)):
            currProfit = prices[r] - prices[l]
            if currProfit > 0:
                maxProfit = max(maxProfit, currProfit)
            
            else:
                l = r

        return maxProfit