# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # find the nodes with bsearch
        p_aux, q_aux = root, root
        par_p, par_q = None, None
        lowestAnc = root

        while (p_aux and p_aux.val != p.val 
                or q_aux and q_aux.val != q.val):
            par_p, par_q = p_aux, q_aux
            
            if p_aux.val > p.val and q_aux.val > q.val:
                lowestAnc = lowestAnc.left
                p_aux = p_aux.left
                q_aux = q_aux.left
            
            elif p_aux.val < p.val and q_aux.val < q.val:
                lowestAnc = lowestAnc.right
                p_aux = p_aux.right
                q_aux = q_aux.right
            
            else:
                return lowestAnc

        print(p_aux.val, par_p.val)
        print(q_aux.val, par_q.val)

        return lowestAnc