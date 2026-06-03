class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(curSum, i, path):
            if curSum == target:
                res.append(path[:])
                return
            if i >= len(candidates) or curSum > target:
                return
            
            path.append(candidates[i])
            backtrack(curSum + candidates[i], i + 1, path)
            path.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(curSum, i + 1, path)

        backtrack(0, 0, [])
        return res
