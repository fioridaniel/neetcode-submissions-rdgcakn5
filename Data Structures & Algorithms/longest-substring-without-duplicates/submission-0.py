class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maior_sub = 0
        n = len(s)
        seen = set()

        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            maior_sub = max(maior_sub, r - l + 1)
        
        return maior_sub