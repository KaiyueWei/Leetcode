"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda interval : interval.start)
        nonOverlap = []
        for interval in intervals:
            if not nonOverlap or nonOverlap[-1].end <= interval.start:
                nonOverlap.append(interval)
            else:
                return False
        return True
