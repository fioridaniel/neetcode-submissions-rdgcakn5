# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if root.val == subRoot.val:
            if self.sameTree(root, subRoot):
                return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, r: Optional[TreeNode], sr: Optional[TreeNode]):
        if not r or not sr:
            if r or sr:
                return False
            
            return True
        
        if r.val != sr.val:
            return False

        return self.sameTree(r.left, sr.left) and self.sameTree(r.right, sr.right)
