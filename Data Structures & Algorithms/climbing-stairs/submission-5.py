class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        first, second = 1, 2
        res = first + second
        
        for _ in range(3, n + 1):
            res = first + second
            first, second = second, res
        
        return res