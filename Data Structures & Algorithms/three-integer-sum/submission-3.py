class Solution:
    # O(n)
    def twoPointersSum(self, i, l, r, target, nums, res):
        while l < r:
            curSum = nums[l] + nums[r]

            if curSum < target:
                l += 1
            elif curSum > target:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                # r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # O(nlogn)
        
        for i in range(len(nums) - 1):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            self.twoPointersSum(i, i + 1, len(nums) - 1, -nums[i], nums, res)
        
        return res # O(n²)