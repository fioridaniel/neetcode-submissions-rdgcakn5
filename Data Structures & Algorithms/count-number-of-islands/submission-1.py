class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        numIslands = 0

        def getNeighbors(i, j):
            res = []
            if i - 1 >= 0:
                res.append((i - 1, j))    
            if j - 1 >= 0:
                res.append((i, j - 1))
            if i + 1 < len(grid):
                res.append((i + 1, j))
            if j + 1 < len(grid[0]):
                res.append((i, j + 1))
            return res

        def dfs(i, j):
            if (i, j) in visited or grid[i][j] == "0":
                return
            
            visited.add((i, j))

            for ni, nj in getNeighbors(i, j):
                dfs(ni, nj)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if  grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    numIslands += 1

        return numIslands