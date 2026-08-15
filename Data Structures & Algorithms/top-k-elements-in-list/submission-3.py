class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        sorted_nums = sorted(cnt.keys(), key=lambda x: cnt[x], reverse=True)
        return sorted_nums[:k]
