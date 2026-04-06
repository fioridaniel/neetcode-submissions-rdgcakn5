class Solution:
    import math

    def maxProduct(self, nums: List[int]) -> int:
        maxVal = -math.inf
        currMin, currMax = 1, 1

        for n in nums:
            if n == 0:
                maxVal = max(maxVal, 0)
                currMax, currMin = 1, 1
            
            aux1 = n * currMax
            aux2 = n * currMin
            currMax = max(aux1, aux2, n)
            currMin = min(aux1, aux2, n)
            maxVal = max(maxVal, currMax)

        return maxVal