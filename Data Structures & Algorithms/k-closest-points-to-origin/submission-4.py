class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calcDist(px, py):
            print(math.sqrt(pow(px, 2) + pow(py, 2)))
            return math.sqrt(pow(px, 2) + pow(py, 2))
        
        dist = [] 
        for i in range(len(points)):
            dist.append((calcDist(points[i][0], points[i][1]), i))

        heapq.heapify(dist)
        
        res = []
        for _ in range(k):
            min_dist, idx = heapq.heappop(dist)
            res.append(points[idx])
        
        return res