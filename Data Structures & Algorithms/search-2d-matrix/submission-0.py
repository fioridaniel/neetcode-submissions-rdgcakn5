class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        # find the correct row => O(log(n))
        targetRow = -1
        l, r = 0, rows - 1
        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][cols - 1] == target:
                return True
            
            elif target < matrix[mid][cols - 1]:
                if matrix[mid][0] <= target:
                    targetRow = mid
                    break
                r = mid - 1
                
            elif target > matrix[mid][cols - 1]:
                l = mid + 1

        # find the correct col => O(log(m))
        l, r = 0, cols - 1
        while l <= r:
            mid = (l + r) // 2

            if matrix[targetRow][mid] == target:
                return True
            
            elif target < matrix[targetRow][mid]:
                r = mid - 1
                
            else:
                l = mid + 1
        
        return False