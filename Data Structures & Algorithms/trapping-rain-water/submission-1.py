class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ## leftMax: from 0  to i -1
        ## rightMax: from i + 1 to n - 1
        leftMax = [0] * n
        rightMax = [0] * n
        for i in range(1, n):
            leftMax[i] = max(leftMax[i-1], height[i-1]) 
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i+1])
        
        res = 0
        for i in range(n):
            s = min(leftMax[i], rightMax[i]) - height[i]
            if s > 0:
                res += s
        return res
            


        





            
            


    



        