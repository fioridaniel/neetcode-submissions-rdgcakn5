class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # se o elemento atual nao for 
            # maior que o subarray (soma), nao troca   

        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        
        return maxSub