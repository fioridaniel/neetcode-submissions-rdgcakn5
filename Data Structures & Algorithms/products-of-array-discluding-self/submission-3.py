class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        # calculate the prefix
        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i - 1]
            res[i] = prod

        # calculate the sufix
        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1]
            res[i] *= prod

        return res