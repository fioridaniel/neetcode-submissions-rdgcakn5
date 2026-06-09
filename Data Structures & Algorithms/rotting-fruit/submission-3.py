class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh_oranges = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        def addToPath(r, c):
            nonlocal fresh_oranges
            if ((0 > r or r >= ROWS) or (0 > c or c >= COLS) 
                or grid[r][c] != 1):
                return
            
            grid[r][c] = 2
            fresh_oranges -= 1
            q.append((r, c))

        # bfs
        minutes = 0
        while q and fresh_oranges > 0:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()

                addToPath(r + 1, c)
                addToPath(r - 1, c)
                addToPath(r, c + 1)
                addToPath(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return minutes
