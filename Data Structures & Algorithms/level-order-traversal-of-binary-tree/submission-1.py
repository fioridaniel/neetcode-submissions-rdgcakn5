# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = []     
        queue.append(root)

        while queue:          
            lvl_len = len(queue)
            curr_nodes = []

            for _ in range(lvl_len):
                node = queue.pop(0)
                curr_nodes.append(node.val)
                l = node.left
                r = node.right

                if l:
                    queue.append(l)
                
                if r:
                    queue.append(r)
            res.append(curr_nodes)
            
        return res


        
                    