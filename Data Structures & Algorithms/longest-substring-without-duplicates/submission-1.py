class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        maxLenght = 0
        l = 0
        for r in range(len(s)):
            while s[r] in characters:
                characters.remove(s[l])
                l += 1
            
            characters.add(s[r])
            maxLenght = max(maxLenght, r - l + 1)

        return maxLenght