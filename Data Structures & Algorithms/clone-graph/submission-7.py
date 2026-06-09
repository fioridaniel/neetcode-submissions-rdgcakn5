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

        oldToNew = {}

        def nodeMap(curr, visited):
            if curr in visited:
                return
            
            oldToNew[curr] = Node(curr.val)
            visited.add(curr)

            for nei in curr.neighbors:
                nodeMap(nei, visited)

        def dfs(curr, visited):
            if curr in visited:
                return
            
            newNode = oldToNew[curr]
            visited.add(curr)

            for nei in curr.neighbors:
                newNode.neighbors.append(oldToNew[nei])
                dfs(nei, visited)

        nodeMap(node, set())
        dfs(node, set())

        return oldToNew[node]