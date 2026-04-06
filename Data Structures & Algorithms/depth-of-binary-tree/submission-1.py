# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxDepth = 1

        def backtrack(root, currDepth):
            nonlocal maxDepth

            if not root:
                maxDepth = max(maxDepth, currDepth)
                return

            backtrack(root.left, currDepth + 1)
            backtrack(root.right, currDepth + 1)

        backtrack(root, 0)

        return maxDepth