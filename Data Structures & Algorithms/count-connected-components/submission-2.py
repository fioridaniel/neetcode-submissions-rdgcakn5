class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgesMap = {}

        for i in range(n):
            edgesMap[i] = []

        for e in edges:
            a, b = e
            edgesMap[a].append(b)
            edgesMap[b].append(a)
        
        print(edgesMap)
        visited = set()
        
        def dfs(node, parent):
            if node in visited:
                return

            visited.add(node)

            for nei in edgesMap[node]:
                if nei == parent:
                    continue
                dfs(nei, node)

        count = 0
        for i in range(n):
            if i in visited:
                continue
            
            dfs(i, -1)
            count += 1

        return count