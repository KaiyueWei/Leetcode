class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval : interval[0])
        merged = []
        for i in range(len(intervals)):
            if merged and merged[-1][1] >= intervals[i][0]:
                merged[-1][0] = min(merged[-1][0], intervals[i][0])
                merged[-1][1] = max(merged[-1][1], intervals[i][1])
            else:
                merged.append(intervals[i])
        return merged