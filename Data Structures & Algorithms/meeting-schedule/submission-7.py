"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.end)
        l = 0

        for r in range(1, len(intervals)):
            if intervals[r].start < intervals[l].end:
                return False
            
            l = r

        return True