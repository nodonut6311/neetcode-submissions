class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            f = heapq.heappop(maxHeap)
            s = heapq.heappop(maxHeap)

            if s > f:
                heapq.heappush(maxHeap, f - s)
        
        maxHeap.append(0)
        return abs(maxHeap[0])