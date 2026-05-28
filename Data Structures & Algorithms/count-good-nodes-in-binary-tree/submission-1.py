# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(curr, maxVal):
            nonlocal count

            if not curr:
                return
            
            if curr.val >= maxVal:
                count += 1
                maxVal = curr.val
                
            dfs(curr.left, maxVal)
            dfs(curr.right, maxVal)
            
        
        dfs(root, root.val)

        return count