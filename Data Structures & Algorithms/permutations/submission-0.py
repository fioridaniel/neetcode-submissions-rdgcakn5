class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path, elems):
            if not elems:
                res.append(path[:])
                return

            for n in list(elems):
                elems.remove(n)
                path.append(n)
                backtrack(path, elems)

                elems.add(n)
                path.pop()
                # backtrack(path, elems)
            
        backtrack([], set(nums))
        return res