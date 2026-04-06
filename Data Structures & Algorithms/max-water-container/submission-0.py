class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        l = 0
        r = n  - 1

        while r > l:
            maxArea = max(maxArea, (r - l) * min(heights[l], heights[r]))
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1

        return maxArea