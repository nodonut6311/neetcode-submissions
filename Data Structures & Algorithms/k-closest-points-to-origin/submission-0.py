class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        n = len(points)
        for i in range(n):
            x = points[i][0]
            y = points[i][1]
            heapq.heappush(res, (-math.sqrt((x*x) + (y*y)), [x, y]))
        
        while len(res) > k:
            heapq.heappop(res)
        
        return [point for _, point in res]