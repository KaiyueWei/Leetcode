class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [-1]   # sentinel
        n = len(heights)
        ## The rectangle spans between the new top of stack and current index.
        for i, h in enumerate(heights):
            while stack[-1] != -1 and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = n - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area
        
        