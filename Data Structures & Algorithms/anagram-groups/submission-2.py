class Solution:
    def isAnagram(self, s, t):
        sMap, tMap = {}, {}

        if len(s) != len(t):
            return False

        for c in s:
            sMap[c] = 1 + sMap.get(c, 0)
        
        for c in t:
            tMap[c] = 1 + tMap.get(c, 0)

        return sMap.items() == tMap.items()

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        visited = set()

        for i in range(len(strs)):
            if strs[i] in visited:
                continue

            temp = [strs[i]]
            visited.add(strs[i])
            for j in range(i + 1, len(strs)):
                if self.isAnagram(strs[i], strs[j]):
                    temp.append(strs[j])
                    visited.add(strs[j])
            
            res.append(temp)
        
        return res