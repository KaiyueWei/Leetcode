class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n <= 1:
            return 0
        intervals.sort(key = lambda interval: interval[0])
        nonOverlap = []
        for interval in intervals:
            if not nonOverlap or nonOverlap[-1][1] <= interval[0]:
                nonOverlap.append(interval)
            else:
                nonOverlap[-1] = [nonOverlap[-1][0], min(interval[1], nonOverlap[-1][1])]
        return (n - len(nonOverlap))


        