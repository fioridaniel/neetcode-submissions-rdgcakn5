# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        curr_level = 0
        count = 0
        res = [root.val]

        while queue:  
            level_lenght = len(queue)
            flag = False
            
            for _ in range(level_lenght):    
                node = queue.popleft()
                print(f'val: {node.val}, level: {curr_level}')

                left, right = node.left, node.right
                if right:
                    queue.append(right)
                    if not flag:
                        flag = True
                        res.append(right.val)
                if left:
                    queue.append(left)
                    if not flag:
                        flag = True
                        res.append(left.val)
            curr_level += 1
        
        return res
                