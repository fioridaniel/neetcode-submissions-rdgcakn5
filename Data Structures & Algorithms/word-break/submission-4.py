class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True # string vazia

        for i in range(1, n + 1):
            for w in wordDict:
                lw = len(w)
                if i - lw >= 0 and s[i - lw : i] == w and dp[i - lw]:
                    dp[i] = True
                    break

        return dp[n]