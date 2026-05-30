class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, aux):
            nonlocal res
            
            if i >= len(nums):
                res.append(aux[:])
                return

            aux.append(nums[i])
            backtrack(i + 1, aux)
            
            aux.pop()
            backtrack(i + 1, aux)
        
        backtrack(0, [])

        return res