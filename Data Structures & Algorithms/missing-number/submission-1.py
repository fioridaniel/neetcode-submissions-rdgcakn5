class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        real_acc = sum(range(1, n + 1))
        acc = sum(nums)

        return real_acc - acc