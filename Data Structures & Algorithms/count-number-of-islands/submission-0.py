class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] 
        visited = set()
        islands = 0

        def bfs(r, c):
            dq = collections.deque()
            dq.append((r, c))
            visited.add((r, c))
            
            while dq:
                r, c = dq.popleft()
                # nao pode ter diagonais
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc 
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if (nr, nc) not in visited and grid[nr][nc] == "1":
                            visited.add((nr, nc))
                            dq.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)       
                    islands += 1

        return islands