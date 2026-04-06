class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maior_sub = 0
        n = len(s)
        count = {}

        for r in range(n):
            count[s[r]] = 1 + count.get(s[r], 0) # 0 se tiver vazio
            while k < (r - l + 1) - max(count.values()):
                count[s[l]] -= 1
                l += 1
            
            maior_sub = max(maior_sub, r - l + 1)
        
        return maior_sub