class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # numero de nós visitados = n + 1 => grafo eh conectado
        # aplicar dfs ou bfs no grafo e ver se nao tem ciclos
        broMap = { i:[] for i in range(n) }
        for e in edges:
            if e[0] == e[1]:
                return False
            broMap[e[0]].append(e[1])
            broMap[e[1]].append(e[0])
        print(broMap)

        visited = set()  
        stack = [(0, -1)]  

        while stack:  
            node, par = stack.pop()  
            if node not in visited:
                visited.add(node)  
                print(node)        
                for nei in broMap[node]:
                    if nei not in visited:
                        stack.append((nei, node))
            else:
                return False
        
        return len(visited) == n