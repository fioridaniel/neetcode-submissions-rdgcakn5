class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construir o grafo => O(len(prerequisites))
        # aplicar dfs => O(len(prerequisites))
        # ... O(len(prerequisites))

        graph = {i: [] for i in range(numCourses)}
        
        for a, b in prerequisites:
            graph[a].append(b)
        
        visited = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            if graph[crs] == []:
                return True

            visited.add(crs)
            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            graph[crs] = []
            return True

        if not prerequisites:
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True