class Solution:
    def countSubstrings(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        
        while r < len(s):
            res += self.countPali(s, l, r)
            res += self.countPali(s, l, r + 1)
            l, r = l + 1, r + 1
        
        return res

    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res