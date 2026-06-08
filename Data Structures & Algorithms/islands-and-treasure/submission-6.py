class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        q, visited = deque(), set()

        def addPath(i, j, dist):
            if ((0 > i or i >= ROWS) or (0 > j or j >= COLS) 
                or grid[i][j] == -1 or (i, j) in visited):
                return 

            grid[i][j] = dist
            q.append([i, j])
            visited.add((i, j))
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append([i, j])
                    visited.add((i, j))
        
        # bfs 
        dist = 1
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                addPath(i + 1, j, dist)
                addPath(i - 1, j, dist)
                addPath(i, j + 1, dist)
                addPath(i, j - 1, dist)
            dist += 1
