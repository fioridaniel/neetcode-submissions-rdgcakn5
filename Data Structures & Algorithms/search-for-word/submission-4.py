class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def getNeighbors(i, j):
            neighbors = []
            
            if i + 1 < len(board):
                neighbors.append((i + 1, j))
            if i - 1 >= 0:
                neighbors.append((i - 1, j))
            if j + 1 < len(board[0]):
                neighbors.append((i, j + 1))
            if j - 1 >= 0:
                neighbors.append((i, j - 1))
            
            return neighbors

        def dfs(i, j, curr, visited):
            if curr < len(word) and board[i][j] != word[curr]:
                return False
            if curr == len(word) - 1:
                return True   

            visited.add((i, j))

            neighbors = getNeighbors(i, j)
            for nei in neighbors: 
                if nei not in visited:
                    ni, nj = nei
                    if dfs(ni, nj, curr + 1, visited):
                        return True
            
            visited.remove((i, j))
            
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0, set()):
                    return True
        
        return False