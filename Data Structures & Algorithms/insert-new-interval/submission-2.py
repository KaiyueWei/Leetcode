class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []
        # no overlap
        # cur_end < new_start
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        # overlapping starts with i as long as new_end >= cur_start
        # new_start < end, new_end >= start
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
        ## no overlap
        # new_end < cur_start
        while i < n:
            res.append(intervals[i])
            i += 1
        return res