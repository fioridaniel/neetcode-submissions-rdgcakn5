class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculate the prefix
        prefix = [1] * len(nums)
        prefix[0] = 1
        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i - 1]
            prefix[i] = prod

        print(prefix)

        # calculate the sufix
        sufix = [1] * len(nums)
        sufix[len(nums) - 1] = 1
        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1]
            sufix[i] = prod

        print(sufix)

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * sufix[i])

        return res