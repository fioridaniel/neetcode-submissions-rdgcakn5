class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def backtrack(j, i):        
            if i >= len(s):
                if i == j:
                    res.append(part[:])
                return
            
            if isPalindrome(j, i):
                part.append(s[j : i + 1])
                backtrack(i + 1, i + 1)
                part.pop()
            
            backtrack(j, i + 1)

        backtrack(0, 0)
        return res