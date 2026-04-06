class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        n = len(prices)
        profit = 0

        while right < n:
            if prices[left] > prices[right]:
                left = right
            elif prices[left] < prices[right]:
                profit = max(prices[right] - prices[left], profit) 
            right += 1
        
        return profit