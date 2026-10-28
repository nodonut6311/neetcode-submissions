class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        maxHeap = [(-c, n) for n, c in cnt.items()]
        heapq.heapify(maxHeap)

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(maxHeap)[1])

        return ans