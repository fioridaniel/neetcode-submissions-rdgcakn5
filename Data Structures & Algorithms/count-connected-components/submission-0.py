class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # realizar uma busca dfs em cada componente?
        # casos que dariam problema =>
            # - loop no proprio no? sol: ignorar?

        adjList = { i: [] for i in range(n) }
        for e in edges:
            if e[0] == e[1]: # ignora self loop 
                continue
            adjList[e[0]].append(e[1])
            adjList[e[1]].append(e[0])

        num_components = 0
        visited = set()

        for i in range(n):
            if i in visited:
                continue 
            
            s = [i]
            num_components += 1
            while s:
                node = s.pop()
                if node not in visited:
                    visited.add(node)
                    for nei in adjList[node]:
                        s.append(nei)

        return num_components

        

