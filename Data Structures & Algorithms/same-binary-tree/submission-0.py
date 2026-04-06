# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res = True
        def backtrack(p, q):
            nonlocal res
            
            if not p or not q:
                if p or q:
                    res = False
                    return
            
            if p and q:
                if p.val != q.val:
                    res = False
                    return
            
            if not p and not q:
                return

            backtrack(p.left, q.left)
            backtrack(p.right, q.right)

        backtrack(p, q)
        return res
            