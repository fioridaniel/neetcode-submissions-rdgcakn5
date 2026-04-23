# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0

        if not root:
            return maxDepth

        def dfs(node, depth):    
            nonlocal maxDepth
            if not node:
                maxDepth = max(maxDepth, depth - 1)
                return 

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 1)

        return maxDepth