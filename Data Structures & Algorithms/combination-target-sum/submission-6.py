class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        count = [0] * len(nums)
        countSet = set()

        def backtrack(curSum, path, count):
            if curSum == target:
                tCount = tuple(count)
                if tCount not in countSet:
                    res.append(path[:])
                    countSet.add(tCount)
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

