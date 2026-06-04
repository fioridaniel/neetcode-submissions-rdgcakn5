class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(i, j, path):
            if j > n:
                return
            if i == n and j == n:
                res.append(path)
                return
            
            if i >= j and i < n:
                backtrack(i + 1, j, path + "(")

            backtrack(i, j + 1, path + ")")
        
        backtrack(0, 0, "")
        return res

        