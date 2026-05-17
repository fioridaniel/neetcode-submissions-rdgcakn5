class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        for i in range(26):
            count[i] = 0

        maxLenght = 0

        l = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord('A')] += 1

            most_freq = max(count.values()) 

            while l < r and (r - l + 1) - most_freq > k:
                count[ord(s[l]) - ord('A')] -= 1
                l += 1
                most_freq = max(count.values())
            
            maxLenght = max(maxLenght, r - l + 1)

        return maxLenght