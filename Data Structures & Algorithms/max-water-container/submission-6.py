class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        res = 0
        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            cur = w * h
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            res = max(cur, res)
        return res

             