"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        q = []    
        oldToNew = {}
        
        q.append(node)
        oldToNew[node] = Node(node.val)

        while q:
            n = q.pop(0)

            for nei in n.neighbors:
                if nei not in oldToNew:
                    oldToNew[nei] = Node(nei.val)
                    q.append(nei)
                oldToNew[n].neighbors.append(oldToNew[nei])
        
        return oldToNew[node]

