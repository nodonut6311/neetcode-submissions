class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        res = 1
        l = 0

        for r in range(1, len(intervals)):
            if intervals[r][0] >= intervals[l][1]:
                res += 1
                l = r
        
        return (len(intervals) - res)