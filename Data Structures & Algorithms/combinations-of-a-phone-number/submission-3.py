class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def backtrack(i, path):
            if i >= len(digits):
                res.append(path)
                return
            
            for val in digitMap[digits[i]]:
                backtrack(i + 1, path + val)
            
        if digits:
            backtrack(0, "")
        return res