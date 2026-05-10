class Solution:
    """
        temos uma area x. 
        como decidir qual a proxima maior area:
            - escolher a maior barra
            - escolher a maior area
    """
    
    def calcArea(self, h1, h2, dist):
        return min(h1, h2) * dist
            
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0
        
        while l < r:
            maxArea = max(
                maxArea, 
                self.calcArea(heights[l], heights[r], r - l)
            )

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return maxArea
    

