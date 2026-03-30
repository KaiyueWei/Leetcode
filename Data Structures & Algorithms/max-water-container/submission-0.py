class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # shortest bar is the height 
        # distance between two bars is the width
        # water containers can hold: height * width
        maxWater = 0 
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                shortest_height = min(heights[i], heights[j])
                cur_water = shortest_height * abs(i - j)
                maxWater = max(maxWater, cur_water)
        return maxWater
             