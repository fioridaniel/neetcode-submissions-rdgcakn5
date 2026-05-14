class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, grids = defaultdict(set), defaultdict(set), defaultdict(set)

        for i in range(9):
            for j in range(9):
                cell = board[i][j]

                if cell == '.':
                    continue
                
                if cell in rows[i] or cell in cols[j]:
                    return False
                rows[i].add(cell)
                cols[j].add(cell)

                if cell in grids[(i // 3, j // 3)]:
                    return False
                grids[(i // 3, j // 3)].add(cell)

        return True