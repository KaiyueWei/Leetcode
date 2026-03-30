class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        i = 0
        # no overlap
        # interval.end < new.start
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        # overlap: expand the newInterval
        # interval.end >= new.start and interval.start <= new.end
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        # no overlap
        while i < n:
            res.append(intervals[i])
            i += 1
        return res

        
        
        