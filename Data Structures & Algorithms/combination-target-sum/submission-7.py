class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(curSum, path, i):
            if curSum == target:
                res.append(path[:])
                return
            
            if curSum > target or i >= len(nums):
                return

            path.append(nums[i])
            backtrack(curSum + nums[i], path, i)
            
            path.pop()
            backtrack(curSum, path, i + 1)
        
        backtrack(0, [], 0)
        return res

