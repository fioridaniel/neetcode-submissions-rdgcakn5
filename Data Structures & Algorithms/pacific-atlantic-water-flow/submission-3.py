class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pac_set = set()
        atl_set = set()

        def inBounds(r, c):
            if r >= 0 and r < rows and c >= 0 and c < cols:
                return True
            return False
        
        def dfs(r, c, prev, visited):
            if not inBounds(r, c) or (r, c) in visited or prev > heights[r][c]:
                return

            visited.add((r, c))
            
            dfs(r + 1, c, heights[r][c], visited)
            dfs(r, c + 1, heights[r][c], visited)
            dfs(r - 1, c, heights[r][c], visited)
            dfs(r, c - 1, heights[r][c], visited)
        
        for r in range(rows):
            dfs(r, 0, 0, pac_set)
            dfs(r, cols - 1, 0, atl_set)

        for c in range(cols):
            dfs(0, c, 0, pac_set)
            dfs(rows - 1, c, 0, atl_set)

        return list(pac_set.intersection(atl_set))