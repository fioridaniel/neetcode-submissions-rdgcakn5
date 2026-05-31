class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        count = [0] * len(nums)
        countSet = set()

        def backtrack(curSum, path, count):
            if curSum == target:
                if tuple(count) not in countSet:
                    res.append(path[:])
                    countSet.add(tuple(count))
                return
            
            for i in range(len(nums)):
                if nums[i] + curSum > target:
                    continue
                
                count[i] += 1
                path.append(nums[i])
                backtrack(curSum + nums[i], path, count)
                
                count[i] -= 1
                path.pop()
            
        backtrack(0, [], count)
        return res

