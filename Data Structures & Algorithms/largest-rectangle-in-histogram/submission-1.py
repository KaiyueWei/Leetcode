class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                h, j = stack.pop()
                max_area = max(max_area, (i-j)*h)
                start = j
            stack.append((height, start))
        while stack:
            h, j = stack.pop()
            max_area = max(max_area, (n-j)*h)
        return max_area
        
        