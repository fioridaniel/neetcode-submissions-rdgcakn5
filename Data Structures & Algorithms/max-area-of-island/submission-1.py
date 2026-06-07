class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(i, j, area):
            nonlocal maxArea

            if (0 > i or i >= ROWS) or (0 > j or j >= COLS):
                return 0
            if grid[i][j] == 0 or grid[i][j] == '#':
                return 0
            
            grid[i][j] = '#'
            
            return (1 + 
                dfs(i + 1, j, area + 1) +
                dfs(i, j + 1, area + 1) +
                dfs(i - 1, j, area + 1) +
                dfs(i, j - 1, area + 1))
                
        maxArea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                   maxArea = max(maxArea, dfs(i, j, 1))
    
        return maxArea