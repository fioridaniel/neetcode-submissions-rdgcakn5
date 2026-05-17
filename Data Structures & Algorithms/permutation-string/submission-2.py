class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for c in s1:
            count[c] = 1 + count.get(c, 0)

        currWin = {}
        l = 0
        for r in range(len(s2)):    
            c = s2[r]

            if c in count:
                currWin[c] = 1 + currWin.get(c, 0)

                if count == currWin:
                    return True

                while l < r and currWin[c] > count[c]:
                    currWin[s2[l]] -= 1
                    l += 1
            
            else:
                if count == currWin:
                    return True
                
                l = r + 1
                currWin = {}
        
        if count == currWin:
            return True

        return False