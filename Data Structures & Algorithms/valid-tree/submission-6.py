class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgesMap = {}

        for i in range(n):
            edgesMap[i] = []    
        
        for i in range(len(edges)):
            a, b = edges[i]
            edgesMap[a].append(b)
            edgesMap[b].append(a)

        print(edgesMap)

        visited = set()
        
        def dfs(node, parent):
            if node in visited:
                return False
            
            print(node, parent)
            visited.add(node)

            for nei in edgesMap[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
            
